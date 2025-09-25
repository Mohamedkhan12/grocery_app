from flask import Flask, request, jsonify
from flask_cors import CORS
import products_dao
import uom_dao
import orders_dao
from sql_connection import get_sql_connection
import json

app = Flask(__name__)

CORS(app, origins=["http://127.0.0.1:5500"])

connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_product():
    products = products_dao.get_all_product(connection)
    return jsonify(products)

@app.route('/getUOM', methods=['GET'])
def getUOM():
    response = uom_dao.get_uoms(connection)
    return jsonify(response)

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    return jsonify({
        'product_id': return_id
    })

@app.route('/insertOrder', methods=['POST'])
def insertOrder():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    return response

@app.route('/insertProduct', methods=['POST'])
def insertProduct():
    print("Form data received:", request.form)
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    return jsonify({
        'product_id': product_id
    })

@app.route('/updateProduct', methods=['POST'])
def updateProduct():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.update_product(connection, request_payload)
    return jsonify({
        'product_id': product_id
    })

if __name__ == '__main__':
    app.run(port=5000)
