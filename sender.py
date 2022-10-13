import json
from logging import exception
from multiprocessing import connection

try:
    import pika
except exception:
    print("Pika module not found")  

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

def publish(method,body):                    #publishing order to RabitMq
    properties = pika.BasicProperties(method)
    channel.queue_declare(queue='order')
    # channel.basic_publish(exchange='', routing_key='hello', body=json.dumps({'method':method,'body':body}), properties=properties)
    channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(body), properties=properties)
    print(" [x] Sent 'Hello World!'")
    connection.close()
  

# if __name__ == '__main__':
#     publish()