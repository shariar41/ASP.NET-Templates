class Supplier(object): 
     def __init__(self,**kwargs): 
        self.supplier_id = kwargs.get('supplier_id',0) 
        self.supplier_name = kwargs.get('supplier_name','') 
        self.addresss = kwargs.get('address','')