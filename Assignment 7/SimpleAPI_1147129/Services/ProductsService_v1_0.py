from IProductsAPI import IProductsAPI 
from Repository import Repository 
 
class ProductsService_v1_0(IProductsAPI): 
    def __init__(self): 
        self.rep = Repository() 
 
    def get_all_products(self): 
        return self.rep.get_all_products() 
 
    def get_products_by_category(self, catid): 
        return self.rep.get_products_by_category(catid) 
 
    def get_categories(self): 
        return self.rep.get_categories() 
 
    def get_one_product(self, prodid): 
        return self.rep.get_one_product(prodid) 
 
    def insert_product(self, product): 
        return self.rep.insert_product(product) 
 
    def update_product(self, product): 
        return self.rep.update_product(product) 
 
    def delete_product(self, product): 
        return self.rep.delete_product(product) 
 
    def adjust_product_price(self, product_id, newprice): 
        return self.rep.adjust_product_price(product_id, newprice) 
