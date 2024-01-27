-- CTE, placing a query inside a variable, variable is not stored but instead created 
-- every time the CTE is called the statement is packed inside a variable then accessed
WITH variableName as ( SELECT statement )
Accessing the CTE
-- Temp Table, like a CTE to join different tables in a new one etc.
DROP TABLE IF EXISTS #tableName
CREATE TABLE #tableName
INSERT INTO #tableName
-- Trim, left and right trim, clear white spaces
SELECT columnName, TRIM(columnName)
-- Replace
SELECT columnName, REPLACE(columnName, replaceableString, replacement)
-- Substring, similar to string.slice()
SELECT SUBSTRING(columnName,startIndex,moveIndex)
-- Upper and lowercase
SELECT columnName, UPPER(columnName) | LOWER(columnName)
-- Store procedure, arrow function variable to store elements in and call later
CREATE PROCEDURE procedureName
AS 
SELECT*
FROM tableName
EXEC procedureName
-- Alter procedure
ALTER PROCEDURE columnName
@functionArgument
-- Subqueries
SELECT columnName, (SELECT subquery FROM tableName)
-- Creates a temporary table to querry from like CTE but slower
FROM (SELECT columnName FROM tableName)
-- Can querry other tables collumns without joining them
WHERE columnName in (SELECT columnName FROM tableName)