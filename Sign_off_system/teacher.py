import socket
import threading
import json
import time
import logging
import queue
import struct
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from openpyxl import Workbook

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='server.log',
    filemode='a'
)


def is_port_in_use(port, host='0.0.0.0'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.connect_ex((host, port)) == 0


class ServerGUI:
    PORT = 8888
    HEARTBEAT_TIMEOUT = 60
    HEARTBEAT_CHECK_INTERVAL = 15

    def __init__(self):
        self.window = Tk()
        self.window.title("机房签到-教师端")
        self.window.geometry("1024x768")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # 状态管理
        self.running = True
        self.clients = {}  # {(computer, ip): tree_item}
        self.last_activity = {}
        self.client_sockets = []
        self.server = None
        self.socket_lock = threading.Lock()
        self.update_queue = queue.Queue()

        # 初始化组件
        self._init_styles()
        self._create_menu_bar()
        self._create_auto_table()
        self._create_taskbar()

        # 网络初始化
        if not self._init_network():
            return

        # 启动线程
        self.accept_thread = threading.Thread(target=self.accept_clients, daemon=True)
        self.heartbeat_thread = threading.Thread(target=self.heartbeat_checker, daemon=True)
        self.accept_thread.start()
        self.heartbeat_thread.start()

        # GUI定时任务
        self.update_time()
        self.process_update_queue()
        self.center_window()
        self.window.mainloop()

    def _init_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview",
                             background="#F5F5F5",
                             fieldbackground="#F5F5F5",
                             rowheight=25,
                             font=('微软雅黑', 10))
        self.style.map("Treeview", background=[('selected', '#4A90E2')])

    def _create_menu_bar(self):
        menubar = Menu(self.window)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="导出Excel", command=self.save_to_excel)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.on_close)
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="关于", command=self._show_about)
        menubar.add_cascade(label="文件", menu=file_menu)
        menubar.add_cascade(label="帮助", menu=help_menu)
        self.window.config(menu=menubar)

    def _create_auto_table(self):
        container = ttk.Frame(self.window)
        container.pack(fill=BOTH, expand=True, padx=8, pady=8)

        columns = ("computer", "ip", "checkin_class", "checkin_student")
        self.tree = ttk.Treeview(
            container,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headers = [
            ("computer", "计算机名", 180),
            ("ip", "IP地址", 150),
            ("checkin_class", "签到班级", 200),
            ("checkin_student", "签到学生", 150)
        ]

        for col_id, col_text, min_width in headers:
            self.tree.heading(col_id, text=col_text, anchor=CENTER)
            self.tree.column(col_id, width=min_width, anchor=CENTER)

        vsb = ttk.Scrollbar(container, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def _create_taskbar(self):
        taskbar = ttk.Frame(self.window)
        taskbar.pack(fill=X, side=BOTTOM, pady=4)

        self.checkin_count = ttk.Label(taskbar, text="已签到: 0")
        self.checkin_count.pack(side=LEFT, padx=12)

        self.time_label = ttk.Label(taskbar, text="")
        self.time_label.pack(side=RIGHT, padx=12)

    def _init_network(self):
        if is_port_in_use(self.PORT):
            messagebox.showerror("错误", f"端口 {self.PORT} 已被占用")
            self.window.destroy()
            return False

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind(('0.0.0.0', self.PORT))
            self.server.settimeout(1)
            self.server.listen(5)
            logging.info("服务器启动成功")
            return True
        except Exception as e:
            logging.error(f"服务启动失败: {str(e)}")
            self.window.destroy()
            return False

    def accept_clients(self):
        while self.running:
            try:
                client, addr = self.server.accept()
                client.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                                  struct.pack('ii', 1, 0))
                with self.socket_lock:
                    self.client_sockets.append(client)
                threading.Thread(
                    target=self.handle_client,
                    args=(client, addr),
                    daemon=True
                ).start()
                logging.info(f"新连接: {addr}")
            except socket.timeout:
                continue
            except Exception as e:
                if self.running:
                    logging.error(f"接受连接异常: {str(e)}")
                break

    def handle_client(self, client, addr):
        buffer = b''
        try:
            while self.running:
                try:
                    data = client.recv(1024)
                    if not data:
                        break
                    buffer += data

                    # 处理PING请求
                    if buffer.startswith(b'PING'):
                        client.sendall(b'PONG\n')
                        buffer = buffer[5:]
                        continue

                    while b'\n' in buffer:
                        line, buffer = buffer.split(b'\n', 1)
                        try:
                            info = json.loads(line.decode('utf-8'))
                            self.validate_client_info(info, addr)

                            if info['type'] == 'checkin':
                                self.process_checkin(info, addr)
                            elif info['type'] == 'init':
                                self.process_init(info, addr)
                            elif info['type'] == 'heartbeat':
                                self.process_heartbeat(info, addr)

                            response = {"status": "success"}
                            client.sendall(json.dumps(response).encode() + b'\n')

                        except json.JSONDecodeError as e:
                            truncated = line[:50] + b'...' if len(line) > 50 else line
                            logging.warning(f"无效JSON数据: {truncated} 错误: {str(e)}")
                        except Exception as e:
                            logging.error(f"数据处理失败: {str(e)}")

                except (socket.timeout, ConnectionResetError):
                    break
        except Exception as e:
            logging.error(f"客户端处理异常: {str(e)}")
        finally:
            with self.socket_lock:
                if client in self.client_sockets:
                    self.client_sockets.remove(client)
            client.close()

    def validate_client_info(self, info, addr):
        required_fields = {
            'init': ['type', 'computer_name'],
            'checkin': ['type', 'computer_name', 'class', 'name'],
            'heartbeat': ['type', 'computer_name']
        }
        msg_type = info.get('type')
        if msg_type not in required_fields:
            raise ValueError(f"未知消息类型: {msg_type}")
        for field in required_fields[msg_type]:
            if field not in info:
                raise ValueError(f"缺失字段 {field}，来自 {addr}")

    def process_init(self, info, addr):
        key = (info['computer_name'], addr[0])
        if key not in self.clients:
            self.update_queue.put((self._add_tree_item, (key,)))
        self.update_queue.put((self._update_activity, (key,)))

    def _add_tree_item(self, key):
        item = self.tree.insert("", "end", values=(key[0], key[1], "", ""))
        self.clients[key] = item

    def process_checkin(self, info, addr):
        key = (info['computer_name'], addr[0])
        if key not in self.clients:
            self.process_init(info, addr)
        values = (key[0], key[1], info['class'], info['name'])
        self.update_queue.put((self._update_tree_item, (key, values)))
        self.update_queue.put((self._update_activity, (key,)))

    def _update_tree_item(self, key, values):
        if key in self.clients:
            self.tree.item(self.clients[key], values=values)

    def _update_activity(self, key):
        self.last_activity[key] = time.time()
        self.update_checkin_count()

    def process_heartbeat(self, info, addr):
        key = (info['computer_name'], addr[0])
        if key in self.last_activity:
            self.last_activity[key] = time.time()

    def heartbeat_checker(self):
        while self.running:
            current_time = time.time()
            expired = [k for k, t in self.last_activity.items()
                       if current_time - t > self.HEARTBEAT_TIMEOUT]
            if expired:
                self.update_queue.put((self.remove_clients, (expired,)))
            time.sleep(self.HEARTBEAT_CHECK_INTERVAL)

    def remove_clients(self, keys):
        for key in keys:
            if key in self.clients:
                self.tree.delete(self.clients[key])
                del self.clients[key]
            if key in self.last_activity:
                del self.last_activity[key]
        self.update_checkin_count()

    def update_checkin_count(self):
        count = len([k for k in self.clients
                     if self.tree.item(self.clients[k])['values'][3]])
        self.checkin_count.config(text=f"已签到: {count}")

    def update_time(self):
        if self.running:
            self.time_label.config(text=time.strftime("%Y-%m-%d %H:%M:%S"))
            self.window.after(1000, self.update_time)

    def save_to_excel(self):
        if not self.clients:
            messagebox.showwarning("提示", "当前没有可导出的签到数据")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel文件", "*.xlsx")]
        )
        if not path:
            return

        try:
            wb = Workbook()
            ws = wb.active
            ws.append(["计算机名", "IP地址", "班级", "姓名"])
            for key in self.clients:
                values = self.tree.item(self.clients[key])['values']
                ws.append(values)
            wb.save(path)
            messagebox.showinfo("成功", "数据已保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {str(e)}")

    def on_close(self):
        logging.info("正在关闭服务器...")
        self.running = False

        if self.accept_thread.is_alive():
            self.accept_thread.join(timeout=2)
        if self.heartbeat_thread.is_alive():
            self.heartbeat_thread.join(timeout=2)

        self.close_network_connections()
        self.window.destroy()

    def close_network_connections(self):
        with self.socket_lock:
            logging.info("关闭客户端连接...")
            for client in self.client_sockets:
                try:
                    client.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                                      struct.pack('ii', 1, 0))
                    client.shutdown(socket.SHUT_RDWR)
                    client.close()
                except Exception as e:
                    logging.warning(f"关闭连接出错: {str(e)}")
            self.client_sockets.clear()

        if self.server:
            try:
                self.server.close()
            except Exception as e:
                logging.warning(f"关闭服务器出错: {str(e)}")

    def center_window(self):
        self.window.update_idletasks()
        w = self.window.winfo_width()
        h = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() - w) // 2
        y = (self.window.winfo_screenheight() - h) // 2
        self.window.geometry(f"{w}x{h}+{x}+{y}")

    def _show_about(self):
        messagebox.showinfo("关于", "机房签到系统教师端\n版本: 3.2")

    def process_update_queue(self):
        while not self.update_queue.empty():
            func, args = self.update_queue.get()
            try:
                if self.running:
                    func(*args)
            except Exception as e:
                logging.error(f"队列处理异常: {str(e)}")
        if self.running:
            self.window.after(100, self.process_update_queue)


if __name__ == '__main__':
    ServerGUI()