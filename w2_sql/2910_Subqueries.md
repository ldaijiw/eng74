# 29/10/2020

## Subqueries

**A subquery is a nested query inside another SELECT statement**

This allows you to take the results of one query and apply them to another query

A subquery may occur in any of the following clauses
- SELECT: (nested subquery - returns single value only)
- FROM: (inline view) 
- WHERE: (nested subquery)

Example:
```
SELECT CompanyName AS "Customer"
FROM Customers
WHERE CustomerID NOT IN 
	(SELECT CustomerID FROM Orders)
```

```
SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
	(SELECT MAX(UnitPrice) FROM [Order Details] AS "Max Price"
FROM [Order Details]
