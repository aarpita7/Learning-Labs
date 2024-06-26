
USE School;

-- Numeric Functions

-- ROUND
-- Round the average age of students to 1 decimal place.
SELECT ROUND(AVG(age), 1) 
FROM students;

-- CEIL
--  Find the ceiling value of the average age of students.
SELECT CEIL(AVG(age)) 
FROM students;

--  FLOOR
-- Find the floor value of the average age of students.
SELECT FLOOR(AVG(age)) 
FROM students;

--  ABS
-- Task: Calculate the absolute difference between the maximum and minimum age of students.
SELECT ABS(MAX(age) - MIN(age)) 
FROM students;

-- Example 5: POWER
-- Task: Calculate the square of the average age of students.
SELECT POWER(AVG(age), 2) 
FROM students;

-- Example 6: SQRT
-- Task: Calculate the square root of the average age of students.
SELECT SQRT(AVG(age)) 
FROM students;

-- Example 7: RAND
-- Task: Generate a random number.
SELECT RAND(); 

-- String Functions

--  LENGTH
--  Find the length of each student's name.
SELECT name, LENGTH(name) 
FROM students;

--  CONCAT
-- Concatenate the name and gender of each student.
SELECT CONCAT(name, ' (', gender, ')') 
FROM students;

--  UPPER
--  Convert all student names to uppercase.
SELECT name, UPPER(name)
FROM students;

-- : LOWER
--  Convert all student names to lowercase.
SELECT name, LOWER(name)
FROM students;

-- SUBSTRING
--  Extract the first three characters of each student's name.
SELECT name, SUBSTRING(name, 1, 3) 
FROM students;

--  REPLACE
--  Replace 'a' with 'A' in each student's name.
SELECT name, REPLACE(name, 'a', 'A') AS name_replaced
FROM students;

--  TRIM
-- Trim leading and trailing spaces from a sample name (if any).
SELECT name, TRIM('   Arpita   ') 
FROM students
LIMIT 1; 
