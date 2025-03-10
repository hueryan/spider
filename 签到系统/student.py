import socket
import json
import threading
import logging
import time
import re
from tkinter import *
from tkinter import ttk, messagebox

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='client.log',
    filemode='a'
)


class EnhancedClientGUI:
    PORT = 8888
    HEARTBEAT_INTERVAL = 30
    CONNECT_TIMEOUT = 5
    MAX_RETRIES = 5
    RETRY_DELAY_BASE = 2
    STATUS_CHECK_INTERVAL = 3
    FAST_CHECK_INTERVAL = 1.5

    def __init__(self):
        self.window = Tk()
        self.window.title("机房签到-学生端")
        self.window.geometry("420x320")
        self.window.resizable(False, False)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_close)

        self.running = True
        self.computer_name = socket.gethostname()
        self.stop_event = threading.Event()
        self.checkin_thread = None
        self._current_socket = None

        # 初始化界面组件
        self.create_ui()
        self.create_taskbar()
        self.center_window()

        # 设置初始状态为未连接
        self.update_status_ui(False)

        # 启动后台服务
        self.start_network_monitor()
        self.start_heartbeat()
        self.update_time()

        self.window.mainloop()

    def create_ui(self):
        """创建主界面组件"""
        main_frame = ttk.Frame(self.window, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # IP地址输入部分
        ip_frame = ttk.Frame(main_frame)
        ip_frame.pack(fill=X, pady=5)
        ttk.Label(ip_frame, text="教师端IP:").pack(side=LEFT)
        self.ip_entry = ttk.Entry(ip_frame)
        self.ip_entry.insert(0, self.detect_server_ip())
        self.ip_entry.pack(side=LEFT, fill=X, expand=True, padx=5)

        # 状态指示灯（初始红色）
        self.status_light = Canvas(ip_frame, width=24, height=24, bg='white')
        self.light_id = self.status_light.create_oval(2, 2, 22, 22, fill="red")
        self.status_light.pack(side=RIGHT)

        # 班级选择
        class_frame = ttk.Frame(main_frame)
        class_frame.pack(fill=X, pady=5)
        ttk.Label(class_frame, text="选择班级:").pack(side=LEFT)
        self.class_var = StringVar()
        self.class_combobox = ttk.Combobox(
            class_frame,
            textvariable=self.class_var,
            values=['21数据本1', '21计本1'],
            state="readonly"
        )
        self.class_combobox.current(0)
        self.class_combobox.pack(side=LEFT, fill=X, expand=True, padx=5)

        # 姓名输入
        name_frame = ttk.Frame(main_frame)
        name_frame.pack(fill=X, pady=10)
        ttk.Label(name_frame, text="学生姓名:").pack(side=LEFT)
        self.name_entry = ttk.Entry(name_frame)
        self.name_entry.pack(side=LEFT, fill=X, expand=True, padx=5)

        # 签到按钮
        self.btn_submit = ttk.Button(
            main_frame,
            text="立即签到",
            command=self.start_checkin,
            width=15
        )
        self.btn_submit.pack(pady=15)

    def create_taskbar(self):
        """创建底部状态栏"""
        taskbar = ttk.Frame(self.window, padding=(10, 3))
        taskbar.pack(side=BOTTOM, fill=X)

        self.conn_status = ttk.Label(
            taskbar,
            text="教师端状态: 未连接",
            font=('Microsoft YaHei', 9),
            foreground="#F44336"
        )
        self.conn_status.pack(side=LEFT, padx=5)

        self.time_label = ttk.Label(
            taskbar,
            font=('Microsoft YaHei', 9),
            foreground="#666"
        )
        self.time_label.pack(side=RIGHT, padx=5)

    def detect_server_ip(self):
        """自动检测服务器IP"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]
                base_ip = local_ip.rsplit('.', 1)[0]
                return f"{base_ip}.100" if base_ip.count('.') == 2 else "192.168.6.100"
        except Exception:
            return "192.168.6.100"

    def start_network_monitor(self):
        """可靠的网络监测线程"""

        def monitor():
            last_status = False
            time.sleep(0.5)  # 等待界面初始化完成

            while not self.stop_event.is_set():
                try:
                    # 双重检测机制
                    status1 = self.check_server_reachable()
                    time.sleep(0.3)
                    status2 = self.check_server_reachable()

                    current_status = status1 and status2
                except Exception as e:
                    logging.error(f"检测异常: {str(e)}")
                    current_status = False

                if current_status != last_status:
                    self.safe_gui_update(lambda: self.update_status_ui(current_status))
                    last_status = current_status

                interval = self.FAST_CHECK_INTERVAL if not current_status else self.STATUS_CHECK_INTERVAL
                time.sleep(interval)

        threading.Thread(target=monitor, daemon=True).start()

    def check_server_reachable(self):
        """精确检测服务器可达性"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1.5)
                s.connect((self.ip_entry.get(), self.PORT))

                # 服务级验证
                s.sendall(b'PING\n')
                response = s.recv(16).decode().strip()
                return response == 'PONG'
        except (socket.timeout, ConnectionRefusedError):
            return False
        except Exception as e:
            logging.debug(f"连接异常: {str(e)}")
            return False

    def update_status_ui(self, connected):
        """更新状态指示"""
        target_color = "green" if connected else "red"
        status_text = "已连接" if connected else "未连接"
        status_color = "#4CAF50" if connected else "#F44336"

        # 更新指示灯
        self.status_light.itemconfig(self.light_id, fill=target_color)

        # 更新任务栏状态
        self.conn_status.config(
            text=f"教师端状态: {status_text}",
            foreground=status_color
        )

    def start_heartbeat(self):
        """心跳线程"""

        def heartbeat_loop():
            while not self.stop_event.is_set():
                try:
                    if self.check_server_reachable():
                        self.send_heartbeat()
                    time.sleep(self.HEARTBEAT_INTERVAL)
                except Exception as e:
                    logging.error(f"心跳异常: {str(e)}")
                    time.sleep(self.FAST_CHECK_INTERVAL)

        threading.Thread(target=heartbeat_loop, daemon=True).start()

    def send_heartbeat(self):
        """发送心跳包"""
        data = {
            "type": "heartbeat",
            "computer_name": self.computer_name
        }
        return self.send_request(data)

    def start_checkin(self):
        """开始签到流程"""
        current_status = self.check_server_reachable()
        self.update_status_ui(current_status)

        if not current_status:
            self.show_error("教师端不可达，请检查IP地址")
            return

        if not self.validate_input():
            return

        if self.checkin_thread and self.checkin_thread.is_alive():
            messagebox.showwarning("提示", "已有签到请求在处理中")
            return

        self.btn_submit.config(state=DISABLED, text="提交中...")
        self.checkin_thread = threading.Thread(target=self.process_checkin, daemon=True)
        self.checkin_thread.start()

    def process_checkin(self):
        """处理签到逻辑"""
        checkin_data = {
            "type": "checkin",
            "computer_name": self.computer_name,
            "class": self.class_var.get(),
            "name": self.name_entry.get().strip()
        }

        success = False
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                if self.send_request(checkin_data):
                    success = True
                    break
                logging.warning(f"第{attempt}次尝试失败")
                time.sleep(self.RETRY_DELAY_BASE ** attempt)
            except Exception as e:
                logging.error(f"请求异常: {str(e)}")

        self.safe_gui_update(lambda: self.handle_checkin_result(success))

    def send_request(self, data) -> bool:
        """发送网络请求"""
        try:
            self._current_socket = socket.create_connection(
                (self.ip_entry.get(), 8888),
                timeout=self.CONNECT_TIMEOUT
            )
            with self._current_socket as sock:
                sock.sendall(json.dumps(data).encode() + b'\n')
                response = self.receive_response(sock)
                return response and response.get("status") == "success"
        except socket.timeout:
            logging.warning("连接超时")
            return False
        except ConnectionRefusedError:
            logging.warning("连接被拒绝")
            return False
        except Exception as e:
            logging.error(f"网络错误: {str(e)}")
            return False
        finally:
            self._current_socket = None

    def receive_response(self, sock) -> dict:
        """接收服务器响应"""
        buffer = b''
        try:
            sock.settimeout(3)
            while True:
                part = sock.recv(1024)
                if not part:
                    break
                buffer += part
                if b'\n' in buffer:
                    response_line, buffer = buffer.split(b'\n', 1)
                    try:
                        return json.loads(response_line.decode('utf-8'))
                    except json.JSONDecodeError:
                        logging.error("无效的JSON响应")
                        return None
        except socket.timeout:
            logging.warning("响应接收超时")
            return None

    def validate_input(self) -> bool:
        """验证输入有效性"""
        try:
            socket.inet_aton(self.ip_entry.get())
        except socket.error:
            self.show_error("无效的IP地址格式")
            return False

        name = self.name_entry.get().strip()
        if not re.match(r'^[\u4e00-\u9fa5]{2,10}$', name):
            self.show_error("请输入2-10位中文姓名")
            return False
        return True

    def handle_checkin_result(self, success):
        """处理签到结果"""
        self.btn_submit.config(state=NORMAL, text="立即签到")
        if success:
            messagebox.showinfo("成功", "签到成功！")
            self.safe_destroy()
        else:
            messagebox.showerror("错误", "签到失败，请检查网络连接后重试")

    def update_time(self):
        """更新时间显示"""
        if self.running:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.time_label.config(text=current_time)
            self.window.after(1000, self.update_time)

    def safe_gui_update(self, func):
        """线程安全的GUI更新"""
        if self.running and self.window.winfo_exists():
            self.window.after(0, func)

    def show_error(self, message):
        """显示错误提示"""
        self.safe_gui_update(lambda: messagebox.showerror("错误", message))

    def disable_close(self):
        """阻止直接关闭窗口"""
        if self.running:
            messagebox.showinfo("提示", "请先完成签到操作")

    def safe_destroy(self):
        """安全关闭程序"""
        self.running = False
        self.stop_event.set()

        if self._current_socket:
            try:
                self._current_socket.close()
            except Exception as e:
                logging.warning(f"关闭连接异常: {str(e)}")

        if self.checkin_thread and self.checkin_thread.is_alive():
            self.checkin_thread.join(timeout=2)

        try:
            self.window.destroy()
        except TclError:
            pass

    def center_window(self):
        """窗口居中显示"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == '__main__':
    EnhancedClientGUI()