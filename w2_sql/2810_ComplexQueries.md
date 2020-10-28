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

