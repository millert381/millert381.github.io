---
tags:
  - SQL
---

# PIVOT and UNPIVOT Table Example

> **Source:** [SQL SERVER – PIVOT and UNPIVOT Table Examples](https://blog.sqlauthority.com/2008/06/07/sql-server-pivot-and-unpivot-table-examples/)  
> **Author:** [Pinal Dave](https://blog.sqlauthority.com/author/pinaldave/)  
> **Publication Date:** 2008-06-07

## Summary

This article combines content from two of Pinal Dave's previous articles about how to PIVOT and UNPIVOT tables (see references at the end).  I often refer to this article when looking for a simple example of the structure and syntax needed for building a PIVOT query. Since I do not work on data that needs to be PIVOTed very often, being able to refer to this has been a time saver. It's simple enough that I can apply it to the result set I am working on.

## Example

A Jr. DBA asked the following question:
> If we PIVOT any table and UNPIVOT that table do we get our original table?

Dave's answer:
> Yes, you can but not always. When we pivot the table we use aggregated functions. If due to use of this function if data is aggregated, it will be not possible to get original data back.

The following example demostrates his answer.

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

### Result Sets

Selecting and checking entries in table

| Cust | Product | QTY |
| ---- | ------- | --- |
KATE | VEG | 2 |
KATE | SODA | 6 |
KATE | MILK | 1 |
KATE | BEER | 12 |
FRED | MILK | 3 |
FRED | BEER | 24 |
KATE | VEG | 3 |

Pivot Table ordered by PRODUCT

| PRODUCT | FRED | KATE |
| ------- | ---- | ---- |
| BEER | 24 | 12 |
| MILK | 3 | 1 |
| SODA | NULL | 6 |
| VEG | NULL | 5 |

Pivot Table ordered by CUST

| CUST | VEG | SODA | MILK | BEER | CHIPS |
| ---- | --- | ---- | ---- | ---- | ----- |
| FRED | NULL | NULL | 3 | 24 | NULL |
| KATE | 5 | 6 | 1 | 12 | NULL |

Unpivot Table ordered by CUST

| CUST | PRODUCT | QTY |
| ---- | ------- | --- |
| FRED | MILK | 3 |
| FRED | BEER | 24 |
| KATE | VEG | 5 |
| KATE | SODA | 6 |
| KATE | MILK | 1 |
| KATE | BEER | 12 |

## Conclusion

You can see in above example where we are using the SUM aggregated functions. SUM adds up values based on column used in the sum function. In our example Kate and Veg has two entries. In our pivot example with order by Cust the values are summed up. Now when table goes under UNPIVOT operations it transforms the table which is already went under PIVOT operation.

Looking at the final PIVOT – UNPIVOT table is little different from the original table and it contains the sum of the two records which we have observed in the PIVOT table. You can see that result which are displayed in red fonts are summed.

This way we can get the original table back if aggregate functions was not applied on the data or data was in such form that aggregate function might have not made any difference.

## References

Reference : Pinal Dave (<https://blog.sqlauthority.com>), [SQL SERVER – UNPIVOT Table Example](https://blog.sqlauthority.com/2008/05/29/sql-server-unpivot-table-example/), [SQL SERVER – PIVOT Table Example](https://blog.sqlauthority.com/2008/05/22/sql-server-pivot-table-example/)
