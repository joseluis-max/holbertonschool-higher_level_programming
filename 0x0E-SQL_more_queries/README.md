### More Queries.
----

**How to create a new MySQL user?**

```sql
-- Create a new user.
CREATE USER 'newuser'@'localhost' 
IDENTIFIED BY 'password';

-- provide the new user with permissions.
GRANT type_of_permissions 
ON database_name.table_name 
TO 'newuser'@'localhost';

-- reload all the privileges.
FLUSH PRIVILEGES;

-- Delete a user.
DROP USER 'username'@'localhost';
```

**How to manage privileges for a user to a database or table?**

- `ALL PRIVILEGES`- as we saw previously, this would allow a MySQL user full access to a designated database (or if no database is selected, global access across the system)
- `CREATE`- allows them to create new tables or databases
- `DROP`- allows them to them to delete tables or databases
- `DELETE`- allows them to delete rows from tables
- `INSERT`- allows them to insert rows into tables
- `SELECT`- allows them to use the `SELECT` command to read through databases
- `UPDATE`- allow them to update table rows
- `GRANT OPTION`- allows them to grant or remove other users’ privileges

```sql
-- Add permissions.
-- Privileges Levels
-- *.*                       -> Global
-- database_name.*           -> Database
-- database_name.table_name  -> Table
-- see second example.       -> Column
-- see third example.        -> Store routine
-- see fourth example.       -> Proxy.
GRANT type_of_permission [,type_of_permissions]... 
ON database_name.table_name 
TO 'username'@'localhost';

-- Add permissions Column level
GRANT 
SELECT (column_name,column_name, ...), 
UPDATE(column_name) 
ON database_name.table_name 
TO 'username'@localhost;

-- Add permissions Stored Routine level
GRANT EXECUTE 
ON PROCEDURE CheckCredit 
TO 'username'@localhost;

-- Add permissions Proxy level.
GRANT PROXY 
ON root 
TO 'username'@localhost;

-- REVOKE type_of_permission 
ON database_name.table_name 
FROM 'username'@'localhost';

-- reload all the privileges.
FLUSH PRIVILEGES;

-- Review user's current permissions.
SHOW GRANTS FOR 'username'@'localhost';
```

**What’s a `PRIMARY KEY`?**

It is a constraint uniquely identifies each record in a database table. It is a special case of unique keys. Primary keys cannot be `NULL`, and only one primary key in a table.

**What’s a `FOREIGN KEY`?**

A `FOREIGN KEY` in one table points to a `PRIMARY KEY` in another table. It is a referential constraint between two tables. The foreign key identifies a column or a set of columns in one (referencing) table that refers to a column or set of columns in another (referenced) table.

**How to use `NOT NULL` and `UNIQUE` constraints?**

The `UNIQUE` constraint ensures that all data are unique in a column.

```sql
CREATE TABLE Brands(
	Id INTEGER, 
	BrandName VARCHAR(30) UNIQUE
);
```

A column with a `NOT NULL` constraint, cannot have NULL values.

```sql
CREATE TABLE People(
	Id INTEGER, 
	LastName TEXT NOT NULL,
	FirstName TEXT NOT NULL, 
	City VARCHAR(55)
);
```

**How to retrieve datas from multiple tables in one request?**

we need to **join** the tables in a way that matches up the right information from each one to the other.

![SQL-Joins.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/453e35f2-9d8a-4e59-9898-149f6c06451c/SQL-Joins.jpg)

**What are subqueries?**

Sometimes you don’t have enough information available when you design a query to determine which rows you want. In this case, you’ll have to find the required information with a **subquery**.

```sql
SELECT cFirstName, cLastName
        FROM customers
        WHERE cZipCode = ???

SELECT cZipCode
FROM Customers
WHERE cFirstName = 'Wayne' AND cLastName = 'Dick';

SELECT cFirstName, cLastName, cZipCode
        FROM customers
        WHERE cZipCode =        
          (SELECT cZipCode
           FROM customers
           WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');
```

**What are `JOIN` and `UNION`?**

## JOIN:

A join is used for displaying columns with the same or different names from different tables. The output displayed will have all the columns shown individually. That is, the columns will be aligned next to each other.

## UNION:

The UNION set operator is used for combining data from two tables which have columns with the same datatype. When a UNION is performed the data from both tables will be collected in a single column having the same datatype.

![phA2q.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a2c4dcc-345b-49a7-b053-fc41dcbe58eb/phA2q.jpg)