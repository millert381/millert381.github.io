## SQL Server Cursor Example

> **Source:** [SQL Server Cursor Example](https://www.mssqltips.com/sqlservertip/1599/cursor-in-sql-server/)
> **Author:** [Jeremy Kadlec](https://www.mssqltips.com/sqlserverauthor/38/jeremy-kadlec/)
> **Publication Date:** 2020-12-31 (last updated as of 2023-09-20)

## Problem

In my T-SQL code, I always use set based operations. I have been told these types of operations are what SQL Server is designed to process and it should be quicker than serial processing. I know cursors exist, but I am not sure how to use them. Can you provide some cursor examples? Can you give any guidance on when to use cursors? I assume Microsoft included them in SQL Server for a reason so they must have a place where they can be used in an efficient manner.

## Solution

In some circles, cursors are never used.  In others, they are a last resort. And in other groups they are used regularly. In each of these camps, they have different reasons for their stand on cursor usage. Regardless, they probably have a place in particular circumstances and not in others. It boils down to your understanding of the coding technique then your understanding of the problem at hand to make a decision on whether or not cursor-based processing is appropriate or not. To get started let's do the following:

- Look at an example cursor
- Break down the components of the cursor
- Provide additional cursor examples
- Analyze the pros and cons of cursor usage

Let's first provide a SQL Server Cursor example then answer all of the pertinent questions.

### SQL Server Cursor Example

Here is an example SQL Server cursor from this tip Simple script to backup all SQL Server databases where backups are issued in a serial manner:

```sql
DECLARE @name VARCHAR(50) -- database name 
DECLARE @path VARCHAR(256) -- path for backup files 
DECLARE @fileName VARCHAR(256) -- filename for backup 
DECLARE @fileDate VARCHAR(20) -- used for file name 

SET @path = 'C:\Backup\' 

SELECT @fileDate = CONVERT(VARCHAR(20),GETDATE(),112) 

DECLARE db_cursor CURSOR FOR 
SELECT name 
FROM MASTER.dbo.sysdatabases 
WHERE name NOT IN ('master','model','msdb','tempdb') 

OPEN db_cursor  
FETCH NEXT FROM db_cursor INTO @name  

WHILE @@FETCH_STATUS = 0  
BEGIN  
      SET @fileName = @path + @name + '_' + @fileDate + '.BAK' 
      BACKUP DATABASE @name TO DISK = @fileName 

      FETCH NEXT FROM db_cursor INTO @name 
END 

CLOSE db_cursor  
DEALLOCATE db_cursor 
```

### What is a SQL Server Cursor

A SQL Server cursor is a set of T-SQL logic to loop over a predetermined number of rows one at a time.  The purpose for the cursor may be to update one row at a time or perform an administrative process such as SQL Server database backups in a sequential manner.  SQL Server cursors are used for Development, DBA and ETL processes.

### How to Write a Cursor in SQL Server

Creating a SQL Server cursor is a consistent process.  Once you learn the steps you are easily able to duplicate them with various sets of logic to loop through data. Let's walk through the steps:

1. Declare your variables (file names, database names, account numbers, etc.) that you need in the logic and initialize the variables.
This logic would be updated based on your needs.
2. Declare cursor with a specific name (i.e. db_cursor in this tip) that you will use throughout the logic along with the business logic (SELECT statement) to populate the records the cursor will need. The cursor name can be anything meaningful.  This is immediately followed by opening the cursor.
This logic would be updated based on your needs.
3. Fetch a record from cursor to begin the data processing.
NOTE - There are an equal of number of variables declared for the cursor, columns in the SELECT statement and variables in the Fetch logic.  In the example in this tip there is only one variable, one column selected and variable fetched, but if five pieces of data were needed for the cursor then five variables would need to be selected and fetched as well.
4. The data process is unique to each set of logic. This could be inserting, updating, deleting, etc. for each row of data that was fetched. This is the most important set of logic during this process that is performed on each row.
   - This logic would be updated based on your needs.
5. Fetch the next record from cursor as you did in step 3 and then step 4 is repeated again by processing the selected data.
6. Once all of the data has been processed, then you close cursor.
7. As a final and important step, you need to deallocate the cursor to release all of the internal resources SQL Server is holding.

From here, check out the examples below to get started on knowing when to use SQL Server cursors and how to do so.

### Cursor in SQL Server

Based on the code and explanations above, let's break down the SQL Server cursor example and notate which sections would need to be updated when using this code.

```sql
-- 1 - Declare Variables
-- * UPDATE WITH YOUR SPECIFIC CODE HERE *
DECLARE @name VARCHAR(50) -- database name 
DECLARE @path VARCHAR(256) -- path for backup files 
DECLARE @fileName VARCHAR(256) -- filename for backup 
DECLARE @fileDate VARCHAR(20) -- used for file name 

-- Initialize Variables
-- * UPDATE WITH YOUR SPECIFIC CODE HERE *
SET @path = 'C:\Backup\' 

SELECT @fileDate = CONVERT(VARCHAR(20),GETDATE(),112) 

-- 2 - Declare Cursor
DECLARE db_cursor CURSOR FOR 
-- Populate the cursor with your logic
-- * UPDATE WITH YOUR SPECIFIC CODE HERE *
SELECT name 
FROM MASTER.dbo.sysdatabases 
WHERE name NOT IN ('master','model','msdb','tempdb') 

-- Open the Cursor
OPEN db_cursor

-- 3 - Fetch the next record from the cursor
FETCH NEXT FROM db_cursor INTO @name  

-- Set the status for the cursor
WHILE @@FETCH_STATUS = 0  
 
BEGIN  
 -- 4 - Begin the custom business logic
 -- * UPDATE WITH YOUR SPECIFIC CODE HERE *
    SET @fileName = @path + @name + '_' + @fileDate + '.BAK' 
   BACKUP DATABASE @name TO DISK = @fileName 

 -- 5 - Fetch the next record from the cursor
  FETCH NEXT FROM db_cursor INTO @name 
END 

-- 6 - Close the cursor
CLOSE db_cursor  

-- 7 - Deallocate the cursor
DEALLOCATE db_cursor 
```

#### Explanation of Cursor Syntax in SQL Server

Based on the example above, cursors include these components:

- DECLARE statements - Declare variables used in the code block
- SET\SELECT statements - Initialize the variables to a specific value
- DECLARE CURSOR statement - Populate the cursor with values that will be evaluated
  - NOTE - There are an equal number of variables in the DECLARE CURSOR FOR statement as there are in the SELECT statement.  This could be 1 or many variables and associated columns.
- OPEN statement - Open the cursor to begin data processing
- FETCH NEXT statements - Assign the specific values from the cursor to the variables to match the DECLARE CURSOR FOR and SELECT statement
  - NOTE - This logic is used for the initial population before the WHILE statement and then again during each loop in the process as a portion of the WHILE statement
- WHILE statement - Condition to begin and continue data processing
- BEGIN...END statement - Start and end of the code block
  - NOTE - Based on the data processing, multiple BEGIN...END statements can be used
- Data processing - In this example, this logic is to backup a database to a specific path and file name, but this could be just about any DML or administrative logic
- CLOSE statement - Releases the current data and associated locks, but permits the cursor to be re-opened
- DEALLOCATE statement - Destroys the cursor

### Why Use a Cursor in SQL Server

Although using an INSERT, UPDATE or DELETE statement to modify all of the applicable data in one transaction is generally the best way to work with data in SQL Server, a cursor may be needed for:

- Iterating over data one row at a time
- Completing a process in a serial manner such as SQL Server database backups
- Updating data across numerous tables for a specific account
- Correcting data with a predefined set of data as the input to the cursor

### Addition Information
For additional information, view the link to the original article at the top of this page.