# An sql manager for the products table

- Create an object that relates only to the products table in the Northwind database.
- The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defsined as a 'business function'.

- As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files nw_products.py & nw_runner.py and then we will move into creating our object.

Our first requirement...
We've had a requirement for the stock department to print out the average value of all of our stock items.

Away we go....

!!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python.