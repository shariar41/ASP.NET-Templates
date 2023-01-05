class Category(object): 
    def __init__(self,**kwargs): 
        self.category_id = kwargs.get('category_id',0) 
        self.category_name = kwargs.get('category_name','') 