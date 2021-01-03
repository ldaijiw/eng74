# SQL Query HW

[Questions and Requirements](https://github.com/Filipe-p/sql-queries-excercise/blob/master/sql_exercises_homework.md)

### How many orders in NWDB?
```
SELECT COUNT(*) AS 'Number of Orders' FROM Orders;
```
Answer = 830

### How many orders where the ShipCity is Rio de Janeiro?
```
SELECT COUNT(*) AS 'Number of Orders shipping to Rio de Janeiro' FROM Orders
WHERE ShipCity = 'Rio de Janeiro';
```
Answer = 34

### Orders where the ShipCity is Rio de Janeiro or Reims
```
SELECT * AS FROM Orders
WHERE ShipCity IN ('Rio de Janeiro', 'Reims');
```
Answer = 39 (if using ``COUNT(*)``)

### All entries where company name has z or Z in table of customers
```
SELECT * FROM Customers
WHERE CompanyName LIKE '%z%';
```
Answer = 6 (if using ``COUNT(*)``)

### Find names of all companies that do not have FAX numbers. Also find with whom to speak with, contact number, and what city they are based in
```
SELECT CompanyName, ContactName, Phone, City FROM Customers
WHERE Fax IS Null
UNION
SELECT CompanyName, ContactName, Phone, City FROM Suppliers
WHERE Fax IS Null;
```
Answer = 38 (if using ``COUNT(*)``)

### Find information on customers in Paris
```
SELECT * FROM Customers
WHERE City LIKE 'Paris';
```

### Find out clients from Paris, who orders most by quantity? Who are our top 5 clients?

```
SELECT *
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Customers.City = 'Paris';
```

### Need to know more about Paris client, find which deliveries took longer than 10 days. Display business/client name, contact name, all their contact details, as well as number of deliveries that were overdue

```
SELECT
Customers.*,
CASE
	WHEN DATEDIFF(d, OrderDate, ShippedDate) > 10 THEN 'Overdue'
ELSE 'On time'
END AS 'Order Status'
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Customers.City = 'Paris'
```
