-- SQL Operators: Overview and Examples

-- Arithmetic Operators
-- Arithmetic operators perform mathematical operations on numeric data.

-- Addition (+)
SELECT 10 + 5; -- Result: 15

-- Subtraction (-)
SELECT 10 - 5; -- Result: 5

-- Multiplication (*)
SELECT 10 * 5; -- Result: 50

-- Division (/)
SELECT 10 / 5; -- Result: 2

-- Modulus (%)
SELECT 10 % 3; -- Result: 1 (remainder of 10 divided by 3)

-- Comparison Operators
-- Comparison operators are used to compare values.

-- Equal to (=)
SELECT * FROM Employees WHERE Department = 'IT';

-- Not equal to (<> or !=)
SELECT * FROM Employees WHERE Department <> 'IT';

-- Greater than (>)
SELECT * FROM Employees WHERE Salary > 50000;

-- Less than (<)
SELECT * FROM Employees WHERE Salary < 60000;

-- Greater than or equal to (>=)
SELECT * FROM Employees WHERE Salary >= 55000;

-- Less than or equal to (<=)
SELECT * FROM Employees WHERE Salary <= 60000;

-- Logical Operators
-- Logical operators are used to combine multiple conditions.

-- AND
SELECT * FROM Employees WHERE Department = 'IT' AND Salary > 50000;

-- OR
SELECT * FROM Employees WHERE Department = 'IT' OR Department = 'HR';

-- NOT
SELECT * FROM Employees WHERE NOT Department = 'Sales';

-- IN (checks if a value matches any value in a list)
SELECT * FROM Employees WHERE Department IN ('IT', 'HR');

-- BETWEEN (checks if a value is within a range)
SELECT * FROM Employees WHERE Salary BETWEEN 50000 AND 60000;

-- LIKE (pattern matching with wildcards)
SELECT * FROM Employees WHERE FirstName LIKE 'J%';

-- IS NULL (checks for NULL values)
SELECT * FROM Employees WHERE Email IS NULL;

-- IS NOT NULL (checks for non-NULL values)
SELECT * FROM Employees WHERE Email IS NOT NULL;

-- Assignment Operators
-- Assignment operators are used to assign values.

-- Assignment (=)
UPDATE Employees SET Salary = 60000 WHERE EmployeeID = 1;

-- Compound Assignment (+=, -=, *=, /=)
UPDATE Employees SET Salary = 5000 WHERE Department = 'IT';

-- Concatenation Operator
-- Concatenation operator (||) is used to concatenate strings.

SELECT FirstName || ' ' || LastName AS FullName FROM Employees;

-- Comments are used to explain each section and provide examples of SQL operators.
