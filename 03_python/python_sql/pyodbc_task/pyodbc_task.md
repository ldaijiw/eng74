# PYODBC TASK

Task:
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task
 

## SOLUTION NOTES

Import pyodbc and initalise class

```python
import pyodbc

class SQLDatabaseAPI:
    def __init__(self):
        self.start_connection()
```

- Where ``self.start_connection()`` is a method that starts a new connection with default values
```python
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
```

**METHOD TO CREATE A TABLE IN DB**
- In order to create a table in the database, the required parameters are:
    - Table Name (str): Passed as the first argument in the method (``table_name``) 
    - Column Information (dict): Method can accept any number of keyword arguments in the form of ``column_name = 'datatype'`` and form a dictionary (``column_info``) containing all the key info. 
```python
def create_table(self, table_name, **column_info):
    '''
    Creates a new table in current working Database
    table_name (str): Name of table to be created
    Specify column names and datatypes in key=value format
    E.g. name = VARCHAR(16)
    '''
    self.table_name = table_name
    self.table_column_info = column_info
```
- After assigning those two parameters as class attributes, now format all the necessary strings in order to construct the SQL query to be made, in the form of (using example datatypes)
```SQL
CREATE TABLE table_name(
    column1 VARCHAR(255),
    column2 VARCHAR(5),
    column3 INT
    .
    .
    .
    columnN INT
)
```
- Although the tabs and newlines are optional, formatting the string in this way can make debugging the string easier in Python.
```python
    # creates string containing the column information, formatted correctly to be added to the query
    column_info_str = ',\n'.join([f"{column_name} {datatype}" for column_name, datatype in self.table_column_info.items()])
    
    # final string formatted correctly for SQL query
    query = f"CREATE TABLE {table_name}(\n{column_info_str});"

    # execute query
    self.cursor.execute(query)        
```

**METHOD TO INSERT DATA IN TABLE**

- In order to prompt the user for the correct data, create an empty list (``data_values``) and for each item in (``self.table_column_info.items()``) ask the user input with an f-string.
- Found it was necessary to add extra quotes around the user_input if the datatype was VARCHAR()
```python
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
```
- Again the query formatting is:
```SQL
INSERT INTO table_name
(column1, column2, ..., columnN)
VALUES('value1', 'value2', ..., 'valueN')
```
- and so some extra string formatting is required

**METHOD TO DISPLAY TABLE**
```python
def display_table(self):
    # display everything from table
    print(self.cursor.execute(f"SELECT * FROM {self.table_name};").fetchall())
```