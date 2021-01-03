# Connecting to a SQL DB from Python using PYODBC

import pyodbc

# pyodbc driver from Microsoft helps us to connect to SQL instance

# connect to Northwind DB
server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "**"
password = "***"


# server name, DB name, username, and password are required to connect with pyodbc

northwind_connection = pyodbc.connect(
    f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

cursor = northwind_connection.cursor()

# .execute(statement) executes an SQL statement
cursor.execute("SELECT @@VERSION")
# select version of current DB
# fetch one retrieves one row
raw = cursor.fetchone()
print(raw)

# In DB use Customers table

# fetch all retrieves all rows
customer_data = cursor.execute("SELECT * FROM Customers;").fetchall()

for customer_record in customer_data:
    print(customer_record)
    print(type(customer_record))


# combination of loop and control flow to ensure only iterating through data as long as data is available
while True:
    records = customer_data.fetchone()
    # when there are no records left (value is None) stop
    if records is None:
        break
    print(records.UnitPrice)