from flask import Flask 
from flask import jsonify, abort, request  
from flask_httpauth import HTTPBasicAuth # pip install flask_httpauth 
 
#from joblib import dump, load 
from Repository import Repository 
import json 
from MyJsonEncoder import MyJsonEncoder 
from Product import Product 
from ProductsService_v1_0 import ProductsService_v1_0 
import logging 
 
server = Flask(__name__) 
auth = HTTPBasicAuth()  # for authentication 
logging.basicConfig(filename='app.log',level=logging.INFO) 

USER_DATA = {
    "dbuser":"dbuser100"
 }
@auth.verify_password
def verify(username, password):
    if not(username and password):
        return False
    return USER_DATA.get(username)==password

# get all products 
@server.route('/myapi/v1.0/prods', methods=['GET']) 
def get_all_products(): 
    api = ProductsService_v1_0() 
    try: 
        products = api.get_all_products() # list of tuples 
        products_dict_list = [json.dumps(x.__dict__,cls=MyJsonEncoder) for x in products] 
    except Exception as ex: 
        print(str(ex))  # log error 
        abort(500) 
    return jsonify({'prods': products_dict_list}) 
 
# get products by category 
@server.route('/myapi/v1.0/prods/<int:cat_id>', methods=['GET']) 
def get_products_by_cat(cat_id): 
    api = ProductsService_v1_0() 
    try: 
        products = api.get_products_by_category(cat_id) # list of tuples 
        products_dict_list = [json.dumps(x.__dict__,cls=MyJsonEncoder) for x in products] 
    except Exception as ex: 
        print(str(ex))  # log error 
        abort(500) 
    return jsonify({'prods': products_dict_list}) 
 
# get all categries 
@server.route('/myapi/v1.0/categories', methods=['GET']) 
def get_all_categories(): 
    api = ProductsService_v1_0() 
    try: 
        cats = api.get_categories() # list of tuples 
        cats_dict_list = [json.dumps(x.__dict__,cls=MyJsonEncoder) for x in cats] 
    except Exception as ex: 
        print(str(ex))  # log error 
        abort(500) 
    return jsonify({'cats': cats_dict_list}) 
 
 
# get one product 
@server.route('/myapi/v1.0/prods/bypid/<int:product_id>', methods=['GET']) 
def get_product(product_id): 
    api = ProductsService_v1_0() 
    try: 
        prod = api.get_one_product(product_id) # list of tuples 
    except Exception as ex: 
        print(str(ex))   
        logging.exception(str(ex)) # for detailed error logging 
        abort(500) 
    if len(prod) == 0: 
        abort(404) 
    return jsonify({'prod': json.dumps(prod[0].__dict__,cls=MyJsonEncoder)}) 
 
@server.errorhandler(404) # not found 
def not_found(error): 
    return jsonify({'error': 'Not found'}), 404 
 
@server.errorhandler(500)  # internal server error 
def internal_error(error): 
    return jsonify({'error': 'internal server error'}), 404 
 
# add a product - post - create 
@server.route('/myapi/v1.0/prods', methods=['POST']) 
@auth.login_required  # without login results in 401 - unauthorized access 
def create_product(): 
    if not request.json or not 'product_name' in request.json: 
        abort(400) 
    try: 
        pr = Product() 
        pr.product_id = request.json['product_id'] 
        pr.product_name = request.json['product_name'] 
        pr.description = request.json['description'] 
        pr.price = request.json['price']
        pr.stock_level = request.json['stock_level'] 
        pr.category_id = request.json['category_id'] 
        pr.onsale = request.json['onsale'] 
        pr.Discontinued = request.json['Discontinued']
        #pr.supplier_id = request.json['supplier_id'] 
        api = ProductsService_v1_0() 
        prod = api.insert_product(pr) # list of tuples 
    except Exception as ex: 
        #logging.error('Error:' + str(ex))  #for simple error logging 
        logging.exception(str(ex)) # for detailed error logging 
        print(str(ex))   
        abort(500) 
    return jsonify({'prod': json.dumps(pr.__dict__,cls=MyJsonEncoder)}), 201 
 
# update a product - put 
@server.route('/myapi/v1.0/prods/update/<int:product_id>', methods=['PUT']) 
@auth.login_required  # without login results in 401 - unauthorized access 
def update_product(product_id): 
    if not request.json or not 'product_name' in request.json:
        abort(400) 
    try: 
        pr = Product() 
        pr.product_id = product_id 
        pr.product_name = request.json['product_name'] 
        pr.description = request.json['description'] 
        pr.price = request.json['price']
        pr.stock_level = request.json['stock_level'] 
        pr.category_id = request.json['category_id']
        pr.onsale = request.json['onsale'] #added these field due because null is not allowed in db
        pr.Discontinued = request.json['Discontinued']
        #pr.product_id = request.json['product_id'] # pid for where
        #pr.supplier_id = request.json['supplier_id']
        api = ProductsService_v1_0()
        rows = api.update_product(pr)
    except Exception as ex: 
        print(str(ex))
        logging.exception(str(ex)) # log error 
        abort(500) 
    if rows == 0: 
        abort(404) 
    return jsonify({'prod': json.dumps(pr.__dict__,cls=MyJsonEncoder)}), 201 
 
@server.route('/myapi/v1.0/prods/<int:product_id>', methods=['DELETE']) 
@auth.login_required 
def delete_product(product_id): 
    api = ProductsService_v1_0() 
    try:
        rows = api.delete_product(product_id)  
    except Exception as ex: 
        print(str(ex))   
        logging.exception(str(ex)) # log error 
        abort(500) 
    if rows == 0: 
        abort(404) 
    return jsonify({'result': True}) 
 
@server.route('/myapi/v1.0/newprice/<int:product_id>', methods=['PUT']) 
def adjust_product_price(product_id): 
    api = ProductsService_v1_0() 
    newprice = request.json['price'] 
    try: 
        rows = api.adjust_product_price(product_id, newprice) 
    except Exception as ex: 
        print(str(ex))  
        logging.exception(str(ex))  # log error 
        abort(500) 
    if rows == 0: 
        abort(404) 
    return jsonify({'result': True}) 
 
if __name__ == "__main__": 
    server.run(host='127.0.0.1',port=7200,debug=True)#127.0.0.1:7200