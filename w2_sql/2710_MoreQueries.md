# 27/10/2020

### Normal Form

Best practices for designing DBs

**1st Normal Form**: A DB is in 1NF when the following conditions are satisfied:
- Make everything atomic: Data must be presented as small as it can be
- There should be no repeating groups

**2nd Normal Form**
- It is in 1NF
- All non-key attributes are fully functional dependent on the primary key

**3rd Normal Form**
- It is in 2NF
- There is no transitive functional dependency (i.e. a TFD is when a non-key column is functionally dependent on another non-key column, which is functionally dependent on the primary key)

## Querying an SQL DB


