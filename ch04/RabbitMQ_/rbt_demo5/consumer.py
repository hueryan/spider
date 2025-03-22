import pika
import requests
import pickle

QUEUE_NAME = 'scrape'
TOTAL = 100

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
session = requests.Session()

def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {request.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')

while True:
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        request = pickle.loads(body)
        print(f'Get {request}')
        scrape(request)