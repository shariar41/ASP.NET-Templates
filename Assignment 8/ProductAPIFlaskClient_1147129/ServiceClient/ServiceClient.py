import requests 
from requests.auth import HTTPBasicAuth 
import json 
from Models.Product import Product 
from Models.Category import Category 
#from MyJsonEncoder import MyJsonEncoder 
 
class ServiceClient(): 
    def __init__(self): 
        self.base_url = "http://localhost:7200/" 
 
    def get_all_products(self): 
        url = 'myapi/v1.0/prods' 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        #print("entered all products")
        #print(data)
        plist = [Product(json.loads(d)['product_id'], 
                         json.loads(d)['product_name'], 
                         json.loads(d)['description'], 
                         json.loads(d)['price'], 
                         json.loads(d)['stock_level'], 
                         json.loads(d)['category_id'],
                         json.loads(d)['onsale'], 
                         json.loads(d)['Discontinued']) for d in data['prods']] 
        return plist 
 
    def get_products_by_category(self, catid): 
        url = 'myapi/v1.0/prods/' + str(catid) 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        pl = [Product(json.loads(d)['product_id'], 
                         json.loads(d)['product_name'], 
                         json.loads(d)['description'], 
                         json.loads(d)['price'], 
                         json.loads(d)['stock_level'], 
                         json.loads(d)['category_id'],
                         json.loads(d)['onsale'], 
                         json.loads(d)['Discontinued']) for d in data['prods']]
        print(print("entered all products by c"))
        plist = pl
        return plist 
 
    def get_products_by_pid(self, pid): 
        url = 'myapi/v1.0/prods/bypid/' + str(pid) 
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        #print(data)
        prod = Product(json.loads(data['prod'])['product_id'], 
                         json.loads(data['prod'])['product_name'], 
                         json.loads(data['prod'])['description'], 
                         json.loads(data['prod'])['price'], 
                         json.loads(data['prod'])['stock_level'], 
                         json.loads(data['prod'])['category_id'],
                         json.loads(data['prod'])['onsale'], 
                         json.loads(data['prod'])['Discontinued'])
        #print(print("entered all products by pid"))
        return prod 

    def get_categories(self): 
        url = 'myapi/v1.0/categories' 
        #print("entered ")
        r = requests.get(self.base_url + url) 
        json_data = r.text 
        data = json.loads(json_data) 
        #print(data)
        clist = [Category(category_id=json.loads(d)['category_id'], category_name=json.loads(d)['category_name']) for d in data['cats']] 
        return clist 
 
    def add_new_product(self, prod): 
        url = 'myapi/v1.0/prods' 
        #header = ('dbuser', 'dbuser100')
        #print("entered add new prod")
        url2 = self.base_url + url 
        prodjson = json.dumps(prod.__dict__) 
        #print(prodjson)
        r = requests.post(url=url2, json=json.loads(prodjson),auth=('dbuser', 'dbuser100')) 
        r.headers['content-type']
        reply = r.text 
        return reply 

    def update_product(self, prod): 
        url = 'myapi/v1.0/prods/update/' + str(prod.product_id) 
        #header = ('dbuser', 'dbuser100')
        print("entered update prod")
        url2 = self.base_url + url 
        prodjson = json.dumps(prod.__dict__) 
        print(prodjson)
        r = requests.put(url=url2, json=json.loads(prodjson),auth=('dbuser', 'dbuser100')) 
        r.headers['content-type']
        reply = r.text 
        return reply 

    def delete_product(self, product_id): 
        url = 'myapi/v1.0/prods/' + str(product_id) 
        print("enetered")
        #header = ('dbuser', 'dbuser100')
        url2 = self.base_url + url
        r = requests.delete(url=url2,auth=('dbuser', 'dbuser100')) 
        r.headers['content-type']
        reply = r.text 
        return reply 