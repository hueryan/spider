import pika

QUEUE_NAME = 'scrape'
MAX_PRIORITY = 100

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_delete(queue=QUEUE_NAME)  # 删除原有队列（可选，确保数据可丢失）
channel.queue_declare(queue=QUEUE_NAME, arguments={
    'x-max-priority': MAX_PRIORITY,
})

while True:
    """
    data priority # 数据 优先级
    foo 40
    bar 20
    baz 50
    """
    data, priority = input().split()
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, properties=pika.BasicProperties(
        priority=int(priority), # 优先级
    ), body=data)
    print(f"Put {data}")