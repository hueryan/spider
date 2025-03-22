import pika

QUEUE_NAME = "scrape"
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


# 从队列获取数据
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 从队列取出消息
# auto_ack True 表示消费者获取消息之后会自动通知消息队列当前消息已经被处理，可以移除这个消息
channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=callback)

channel.start_consuming()