import pika

QUEUE_NAME = 'scrape'
# 连接 RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 声明频道对象。用它操作队列内消息的生产和消费
channel = connection.channel()
# 声明队列，队列名 'scrape'
channel.queue_declare(queue=QUEUE_NAME)

# 队列添加消息
channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body='Hello World!')