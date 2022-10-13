import json
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.secret_key = "secretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/pizza_house"

mongo = PyMongo(app)

try:
    import pika
except Exception as e:
    print("Pika module not found")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='order')

def callback(ch, method, properties, body):  #callback function
    print(" [x] Received %r" % body)
    data= json.loads(body)
    print("order created in receiver")

    if data['method']=='Order Created':
        print("Order Created")
        order=data['body']
        id = mongo.db.orders.insert({'order': order})
        print("Order added successfully!, Order ID - " + str(id))

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.close()
