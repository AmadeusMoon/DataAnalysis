-- Select DB against which to perform querry
USE DatabaseName

CREATE TABLE TableName
( ColumnName dataType )

-- Select statement and its arguments
SELECT [*, TOP, DISTINCT(Unique values), COUNT(Not Null), AS(Rename), MAX, MIN, AVG] FROM TableName.dbo.table

-- Conditional statement to filter
WHERE conditional [\=,<>,<,>,AND, OR, LIKE, NULL, NOT NULL, IN, *] 

-- Insert data
INSERT INTO TableName VALUES
( Table columns values)

GROUP BY ColumnName
-- Same as where statement but used for the excluded elements 
HAVING COUNT() | MAX() | MIN() | AVG() condition
ORDER BY ColumnName | Index