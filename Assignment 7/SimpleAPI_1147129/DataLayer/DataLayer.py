import pyodbc 
class DataLayer(object): 
    def __init__(self): 
        self.conn_params = 'driver={SQL Server};server=DESKTOP-6TFN4MQ\\SQLEXPRESS;database=ProductsBCBS_1147129;uid=dbuser;pwd=dbuser100' 
 
    def db_insert_update_delete(self,query, params=()): 
        conn = None 
        db = None 
        try: 
            conn = pyodbc.connect(self.conn_params) 
        except pyodbc.Error as e: 
            print(str(e)) 
        else: 
            db = conn.cursor() 
            db.execute(query, params).commit() 
            row_count = db.rowcount # rows affected 
        finally: 
            if conn: 
                conn.close()
        return row_count
 
    def db_select(self,query, params=()): 
        conn = None 
        db = None 
        try: 
            conn = pyodbc.connect(self.conn_params) 
        except pyodbc.Error as e: 

            print(str(e)) 
        else: 
            db = conn.cursor() 
            db.execute(query, params) 
            rows = db.fetchall() 
        finally: 
            if conn: 
                conn.close() 
        return rows