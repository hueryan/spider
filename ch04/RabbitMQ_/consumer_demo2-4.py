import pika

QUEUE_NAME = "scrape"
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


while True:
    # 控制消费频率
    input()
    # 返回元组，body就是数据
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        print(f'Get {body}')
