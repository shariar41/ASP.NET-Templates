from DataLayer import DataLayer 
from Product import Product 
from Category import Category 
 
class Repository(object): 
    def __init__(self): 
        self.datalayer = DataLayer() 
 
    def get_all_products(self): 
        sql = """select productid as product_id, productname as product_name, description, price, stocklevel as stock_level, categoryid as category_id,onsale,Discontinued  from Products""" 
        res = self.datalayer.db_select(sql) # list of tuples 
        resp = [Product(*row) for row in res] 
        return resp 
 
    def get_products_by_category(self, catid): 
        sql = """select productid as product_id, productname as product_name, 
        description, price, stocklevel as stock_level, categoryid as category_id,onsale,Discontinued from Products where CategoryId=?""" 
        param_list = [catid] 
        res = self.datalayer.db_select(sql, param_list) # list of tuples 
        resp = [Product(*row) for row in res] 
        return resp 
 
    def get_categories(self): 
        sql = """select categoryid as category_id, categoryname as category_name from Categories""" 
        res = self.datalayer.db_select(sql) # list of tuples 
        resp = [Category(category_id=row[0], category_name=row[1]) for row in res] 
        return resp 
 
    def get_one_product(self, prodid): 
        sql = """select productid as product_id, productname as product_name, 
        description, price, stocklevel as stock_level, categoryid as category_id,onsale,Discontinued from Products where productid=?""" 
        param_list = [prodid] 
        res = self.datalayer.db_select(sql, param_list) # list of tuples 
        #p1 = Product(category_id=100,category_name='yyy') 
        resp = [Product(*row) for row in res] #made changes
        return resp 
 
    def insert_product(self, product): 
        sql_chk = 'select productname from Products where productname=?' 
        values_chk = [product.product_name] 
        res = self.datalayer.db_select(sql_chk, values_chk) 
        le = len(res) 
        param_list = [product.product_id,product.product_name, product.description, product.price, product.stock_level, product.category_id, product.onsale, product.Discontinued]    
        if len(res) == 0: 
            sql_ins =  ("""INSERT INTO Products(productid,productname, description, price, 
            stocklevel, categoryid, onsale, Discontinued) values (?,?,?,?,?,?,?,?)""")  
            rows = self.datalayer.db_insert_update_delete(sql_ins, param_list) 
        else:  # already exists  
            raise Exception('product name: ' + product.product_name + ' already exists') 
        return rows
 
    def update_product(self, product): 
        sql_chk = 'select productname from Products where productname=?' 
        values_chk = [product.product_name] 
        res = self.datalayer.db_select(sql_chk, values_chk) 
        le = len(res) 
        print("Asdad")
        param_list = [product.product_id,product.product_name, product.description, product.price, product.stock_level, product.category_id, product.onsale, bool(product.Discontinued),product.product_id]    
        if le > 0: 
            print(param_list)
            sql_update =  ("""Update Products Set productid=?,productname=?,description=?,price=?,stocklevel=?,categoryid=?,onsale=?,Discontinued=? where productid=?""")
            rows = self.datalayer.db_insert_update_delete(sql_update, param_list) 
        else:  # already exists  
            raise Exception('product name: ' + product.product_name + ' already exists') 
        return rows
 
    def delete_product(self, product_id):
        param_list = [product_id]
        sql_delete =  ("""delete from Products where productid=?""")
        rows = self.datalayer.db_insert_update_delete(sql_delete, param_list)
        return rows
 
    def adjust_product_price(self, product_id, newprice): 
        param_list = [newprice, product_id]    
        sql_update =  ("""Update Products set price=?  where productid=?""")  
        rows = self.datalayer.db_insert_update_delete(sql_update, param_list) 
        return rows