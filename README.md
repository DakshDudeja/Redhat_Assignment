# Task

This project has 3 api's of Pizza Delivery System.

Main file - app.py
Publisher - sender.py
Subscriber- receiver.py

1. Welcome API
    Path - /welcome
    HTTP method - GET
    Return – “Welcome to Pizza House”
2. Accept order API
    This API takes JSON data as input and stores that order in the MongoDB. API will accept JSON
    input.
    Example input to API - {"order": ["Pizza1", "Pizza2"]}
    Path - /order
    HTTP method - POST
    Return - Order Id
3. Get order details APIs
    1. /getorders - Fetch all the orders in the MongoDB at the given instance.
    HTTP method - GET
    Returns - All orders in the database.
    2. /getorders/<order_id> - Get the order by the order id
    HTTP method - GET
    Returns - Order details of a given order id , 404 Not found if record not present.
    
4. Implementation of order api using RabitMq(message broker)
   - Sender.py: Takes order and send it to a rabbitmq queue.
   - Receiver: Get the order from the queue, save it on a MongoDB.
   - API: Gets data from the DB and show it to the user

# Python - Rabbitmq - Mongodb

> Example using language Python handling queue rabbitmq and save-to mongodb

### Install environment
    + Python [Python](https://www.python.org/downloads) v2.7 to run.
    + Rabbitmq [Rabbit](https://www.rabbitmq.com/download.html)
    + Mongodb [Mongodb](https://www.mongodb.com) v3.4 to run.
    + Run it using Docker RabitMq Image
