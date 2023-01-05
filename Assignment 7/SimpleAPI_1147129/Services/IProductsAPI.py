from abc import abstractmethod 
 
class IProductsAPI(object): 
    @abstractmethod 
    def get_all_products(self): 
        raise NotImplementedError 
 
    @abstractmethod 
    def get__products_by_category(self, catid): 
        raise NotImplementedError 
 
    @abstractmethod 
    def get__categories(self): 
        raise NotImplementedError 
     
    @abstractmethod 
    def get_one_product(self, prodid): 
        raise NotImplementedError 
 
 
    @abstractmethod 
    def insert_product(self, product): 
        raise NotImplementedError 
 
    @abstractmethod 
    def update_product(self, product): 
        raise NotImplementedError 
 
    @abstractmethod 
    def delete_product(self, product): 
        raise NotImplementedError 
 
    @abstractmethod 
    def adjust_product_price(self, product_id, newprice): 
        raise NotImplementedError