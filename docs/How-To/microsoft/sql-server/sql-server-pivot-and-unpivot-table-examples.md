## SQL SERVER – PIVOT and UNPIVOT Table Examples

> **Source:** [SQL SERVER – PIVOT and UNPIVOT Table Examples](https://blog.sqlauthority.com/2008/06/07/sql-server-pivot-and-unpivot-table-examples/)
> **Author:** [Pinal Dave](https://blog.sqlauthority.com/author/pinaldave/)
> **Publication Date:** 2008-06-07

I previously wrote two articles about PIVOT and UNPIVOT tables. I really enjoyed writing about them as it was interesting concept. One of the Jr. DBA at my organization asked me following question.

“If we PIVOT any table and UNPIVOT that table do we get our original table?”

I really think this is good question. Answers is Yes, you can but not always. When we pivot the table we use aggregated functions. If due to use of this function if data is aggregated, it will be not possible to get original data back.

Let me explain this issue demonstrating simple example.

```sql
USE AdventureWorks
GO
-- Creating a Test Table
CREATE TABLE Product(Cust VARCHAR(25), Product VARCHAR(20), QTY INT)
GO
-- Inserting Data into Table
INSERT INTO Product(Cust, Product, QTY)
VALUES('KATE','VEG',2)
INSERT INTO Product(Cust, Product, QTY)
VALUES('KATE','SODA',6)
INSERT INTO Product(Cust, Product, QTY)
VALUES('KATE','MILK',1)
INSERT INTO Product(Cust, Product, QTY)
VALUES('KATE','BEER',12)
INSERT INTO Product(Cust, Product, QTY)
VALUES('FRED','MILK',3)
INSERT INTO Product(Cust, Product, QTY)
VALUES('FRED','BEER',24)
INSERT INTO Product(Cust, Product, QTY)
VALUES('KATE','VEG',3)
GO
-- Selecting and checking entires in table
SELECT *
FROM Product
GO
-- Pivot Table ordered by PRODUCT
SELECT PRODUCT, FRED, KATE
FROM (
SELECT CUST, PRODUCT, QTY
FROM Product) up
PIVOT (SUM(QTY) FOR CUST IN (FRED, KATE)) AS pvt
ORDER BY PRODUCT
GO
-- Pivot Table ordered by CUST
SELECT CUST, VEG, SODA, MILK, BEER, CHIPS
FROM (
SELECT CUST, PRODUCT, QTY
FROM Product) up
PIVOT (SUM(QTY) FOR PRODUCT IN (VEG, SODA, MILK, BEER, CHIPS)) AS pvt
ORDER BY CUST
GO
-- Unpivot Table ordered by CUST
SELECT CUST, PRODUCT, QTY
FROM
(
SELECT CUST, VEG, SODA, MILK, BEER, CHIPS
FROM (
SELECT CUST, PRODUCT, QTY
FROM Product) up
PIVOT
( SUM(QTY) FOR PRODUCT IN (VEG, SODA, MILK, BEER, CHIPS)) AS pvt) p
UNPIVOT
(QTY FOR PRODUCT IN (VEG, SODA, MILK, BEER, CHIPS)
) AS Unpvt
GO
-- Clean up database
DROP TABLE Product
GO
```

ResultSet:

```sql
-- Selecting and checking entires in table
Cust Product QTY
------------------------- -------------------- -----------
KATE VEG 2
KATE SODA 6
KATE MILK 1
KATE BEER 12
FRED MILK 3
FRED BEER 24
KATE VEG 3
```

```sql
-- Pivot Table ordered by PRODUCT
PRODUCT FRED KATE
-------------------- ----------- -----------
BEER 24 12
MILK 3 1
SODA NULL 6
VEG NULL 5
```

```sql
-- Pivot Table ordered by CUST
CUST VEG SODA MILK BEER CHIPS
------------------------- ----------- ----------- ----------- ----------- -----------
FRED NULL NULL 3 24 NULL
KATE 5 6 1 12 NULL
```

```sql
-- Unpivot Table ordered by CUST
CUST PRODUCT QTY
------------------------- -------- -----------
FRED MILK 3
FRED BEER 24
KATE VEG 5
KATE SODA 6
KATE MILK 1
KATE BEER 12 12
```

You can see in above example where we are using the SUM aggregated functions. SUM adds up values based on column used in the sum function. In our example Kate and Veg has two entries. In our pivot example with order by Cust the values are summed up. Now when table goes under UNPIVOT operations it transforms the table which is already went under PIVOT operation.

Looking at the final PIVOT – UNPIVOT table is little different from the original table and it contains the sum of the two records which we have observed in the PIVOT table. You can see that result which are displayed in red fonts are summed.

This way we can get the original table back if aggregate functions was not applied on the data or data was in such form that aggregate function might have not made any difference.

Reference : Pinal Dave (<https://blog.sqlauthority.com>), [SQL SERVER – UNPIVOT Table Example](https://blog.sqlauthority.com/2008/05/29/sql-server-unpivot-table-example/), [SQL SERVER – PIVOT Table Example](https://blog.sqlauthority.com/2008/05/22/sql-server-pivot-table-example/)
