import pika

QUEUE_NAME = 'scrape'
MAX_PRIORITY = 100

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_delete(queue=QUEUE_NAME)
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY,
}, durable=True) # 指定 durable 开启持久化存储

while True:
    """
    data priority # 数据 优先级
    foo 40
    bar 20
    baz 50
    """
    data, priority = input().split()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, properties=pika.BasicProperties(
        priority=int(priority),
        delivery_mode=2, # 持久化，2 消息保存到磁盘
    ), body=data)
    print(f"Put {data}")