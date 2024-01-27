-- Inner join ( only common data by index)
-- Select dbs (import like)
SELECT * 
FROM DBName1.dbo.tableName
-- Instead of join union ( Removes duplicates )
UNION | UNION All ( does not remove duplicates )
SELECT *
FROM DBName2.dbo.tableName AS Alias ( alike storing in variable )
-- Perform join
SELECT * 
FROM DBName1.dbo.tableName
Inner Join DBName2.dbo.tableName
    ON DBName1.columnName = DBName2.columnName
-- Creates Null match for missing values
FULL Outer Join
-- Switch case
CASE
    WHEN condition THEN return
    ELSE
END AS caseReturnColumnName
-- Remove row
DELETE FROM TableName
-- Update
UPDATE DBName1.dbo.tableName
SET columnName = new value 
WHERE columnName = old value | columnName = identifiers
-- Partition, shows count per every row without needing to group them in a single row
SELECT columnName, COUNT(columnName) OVER (PARTITION BY columnName)