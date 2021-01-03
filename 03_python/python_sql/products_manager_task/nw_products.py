import pyodbc

class ProductManager:
    def __init__(self):
        self.start_connection()

       
    def start_connection(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "SA", password = "Passw0rd2018"):
        
        try:
            print("Establishing Connection")
            # connect to server with pyodbc.connect()
            self.db_connection = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}")
            # init cursor to execute queries
            self.cursor = self.db_connection.cursor()
        except:
            print("Something went wrong")
        
        else:
            # if no errors occurs prints following message
            print("Connection Successfully Made")


    def select_query(self, select_details = "*"):
        query_results = self.cursor.execute(f"SELECT {select_details} FROM Products;").fetchall()
        return query_results
        
    
    def average_value(self, column_to_avg):
        query_results = self.cursor.execute(f"SELECT AVG({column_to_avg}) FROM Products;").fetchone()[0]
        return f"AVERAGE VALUE OF {column_to_avg}: {query_results}"

    
    @property
    def table_information(self):
        table_info = self.cursor.execute('''
        SELECT
        TABLE_NAME,
        COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Products';
        ''').fetchall()
        return table_info
        