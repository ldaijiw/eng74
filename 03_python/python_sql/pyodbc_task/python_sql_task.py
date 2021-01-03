import pyodbc

class SQLDatabaseAPI:
    def __init__(self):
        self.start_connection()

    
    def start_connection(self, server = "databases1.spartaglobal.academy", database = "Northwind", username = "**", password = "**"):
        
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
        

    def create_table(self, table_name, **column_info):
        '''
        Creates a new table in current working Database
        table_name (str): Name of table to be created
        Specify column names and datatypes in key=value format
        E.g. name = VARCHAR(16)
        '''
        self.table_name = table_name
        self.table_column_info = column_info

        # creates string containing the column information, formatted correctly to be added to the query
        column_info_str = ',\n'.join([f"{column_name} {datatype}" for column_name, datatype in self.table_column_info.items()])
        
        # final string formatted correctly for SQL query
        query = f"CREATE TABLE {table_name}(\n{column_info_str});"

        # execute query
        self.cursor.execute(query)        


    def insert_data(self):
        '''
        Insert Data into table, will prompt user to input data in correct format
        '''
        if not hasattr(self, 'table_name'):
            self.table_name = input("\nPlease enter a table name to insert data into.\n=> ")
        
        # Empty list of data values which will then be filled with user input
        data_values = []
        
        # Iterate through columns
        for column_name, datatype in self.table_column_info.items():
            # For each column prompt user to input data
            user_data = input(f"\nPlease enter Data for {column_name}\nDATATYPE: {datatype}\n=> ")

            # If datatype is VARCHAR, add extra quotes around data value before appending
            if "VARCHAR" in datatype:
                data_values.append("'" + user_data + "'")
            elif "INT" in datatype:
                data_values.append(user_data)

        # create string for data values, and column names, formatted correctly
        insert_data_str = ', '.join(data_values)
        column_names = ', '.join(self.table_column_info.keys())
        
        # final SQL query string formatted correctly
        query = f"INSERT INTO {self.table_name}\n({column_names})\nVALUES({insert_data_str});"

        # execute query
        self.cursor.execute(query)
    

    def display_table(self):
        # display everything from table
        print(self.cursor.execute(f"SELECT * FROM {self.table_name};").fetchall())



if __name__ == "__main__":
    python_sql_obj = SQLDatabaseAPI()
    python_sql_obj.create_table("ldaijiw_table", name = "VARCHAR(16)" , age = "INT", address = "VARCHAR(32)")
    python_sql_obj.insert_data()
    python_sql_obj.insert_data()
    python_sql_obj.display_table()