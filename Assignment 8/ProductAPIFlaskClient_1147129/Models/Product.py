class Product(object): 
    def __init__(self,*args): 
        if len(args) > 5: 
            self.product_id = args[0] 
            self.product_name = args[1] 
            self.description = args[2] 
            self.price = args[3] 
            self.stock_level = args[4] 
            self.category_id = args[5] 
            self.onsale = args[6]
            self.Discontinued = args[7]
        else: 
            self.product_id = 0 
            self.product_name = '' 
            self.description = '' 
            self.price = 0 
            self.stock_level = 0 
            self.category_id = 100
            self.onsale = False
            self.Discontinued = False