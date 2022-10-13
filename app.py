from queue import Empty
from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from sender import publish
from receiver import callback


app = Flask(__name__)

app.secret_key = "secretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/pizza_house"

mongo = PyMongo(app)


@app.route('/welcome', methods=['GET'])     # welcome page
def welcome():
    return jsonify({"message": "Welcome to Pizza House"})


@app.route('/orderR', methods=['POST'])   #order using RabitMq
def add_order_RabitMq():
    _json = request.json
    _order=_json['order']
    publish("Order Created",_order)       #publishing order to RabitMq
    return jsonify({"message": "Order Created"}) #returning message to user

@app.route('/order', methods=['POST'])  #order using MongoDB
def add_order():
    _json = request.json              #getting order from user
    _order=_json['order']             

    if _order and request.method == 'POST':             #checking if order is not empty
        id = mongo.db.order.insert({'order': _order})    #inserting order to MongoDB
        resp = jsonify("Order added successfully!, Order ID - "+str(id))  #returning message to user
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/getorders', methods=['GET'])     #getting all orders from MongoDB
def get_orders():
    orders = mongo.db.orders.find()            
    resp = dumps(orders)
    return resp

@app.route('/getorder/<id>', methods=['GET'])       #getting order by id from MongoDB
def get_order(id):
    order = mongo.db.orders.find_one({'_id': ObjectId(id)})
    if order is Empty:
        return not_found()
    resp = dumps(order)
    return resp

@app.errorhandler(404)
def not_found(error=None):                         #error handling
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True)
