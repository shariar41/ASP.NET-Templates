import json 
from decimal import Decimal 
 
class MyJsonEncoder(json.JSONEncoder): 
    def default(self, obj): 
        if isinstance(obj, Decimal): # for converting Decimal to float 
            return float(obj) 
        return super(CustomJsonEncoder, self).default(obj) 