# 28/10/2020

## Complex Queries

### String Functions

- SUBSTRING(expression, start, length): e.g. SUBSTRING(name,1,1) for initials
- CHARINDEX(looking_for, where_to_look): e.g. CHARINDEX('a', 'text') searches for 'a' in a column called 'text'
- Left or Right: LEFT(name,5) for first (or last) 5 characters
- LTRIM or RTRIM: Used to remove spaces at beginning or end of a string
- LEN: Returns length of string
- UPPER or LOWER: Convert to upper/lower case
- REPLACE(name, 'old', 'new'): replace characters in string, e.g. REPLACE(name, ' ', '_') replaces space with underscore


### Date Functions

- GETDATE(): Returns date in date(time) format
- SYSDATETIME(): Return date and time of computer being used
- DATEADD(): DATEADD(d,5, OrderDate) adds 5 days
- DATEDIFF(): DATEDIFF(d, OrderDate, ShippedDate) calculate differences between dates
- YEAR(date): Extracts year from date
- MONTH(date): Extracts month from date
- DAY(date): Extracts day from date 

### Case Statements

CASE statements can be useful when you need varying results output based on differing data
```
SELECT CASE
WHEN DATEDIFF(d, OrderDate, ShippedDate) < 10 THEN 'On Time'
ELSE 'Overdue'
END AS 'Status'
FROM Orders;
```

### Aggregate Functions

- AVG
- MIN
- MAX
- SUM

### Filtering

- HAVING is used instead of WHERE when filtering on subtotals/grouped data
- Column Aliases cannot be used in the HAVING clause
- Aggregate functions are not available for use in the WHERE clause due to the SQL processing sequence

```
SELECT SupplierID
SUM(Units),
AVG(Units)
FROM Products
GROUP BY SupplierID
HAVING AVG(Units) > 5;
```
### Joins and Subqueries

**ALIASING TABLES**
```
SELECT *
FROM ORDERS o
JOIN Customers c ON o.customer_id = c.customer_id;
```

![](sql-joins.png)
