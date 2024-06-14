-- SQL 
-- Structured Query Language
-- is a standardized programming language used for managing relational databases.

-- DDL Commands
-- Data Definition Language Commands
-- DDL commands are used to define the structure of database objects.

-- Creating a Database
CREATE DATABASE Company;
USE Company;

-- Creating Tables
-- Example: Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

-- Example: Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2),
    StockQuantity INT
);

-- Altering Tables 
-- Example: Adding a new column
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);


-- Dropping Tables 
-- Example: Drop Employees table
DROP TABLE Employees;

-- DML (Data Manipulation Language) Commands
-- DML commands are used to manipulate data within database objects.

-- Inserting Data 
-- Example: Inserting employees
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES
    (1, 'Arpita', 'Mahapatra', 'IT', 60000),
    (2, 'Sunita', 'Mahapatra', 'HR', 55000),
    (3, 'Shivam', 'Mishra', 'Sales', 62000)
    ;

-- Example: Inserting products
INSERT INTO Products (ProductID, ProductName, Price, StockQuantity)
VALUES
    (101, 'Keyboard', 29.99, 100),
    (102, 'Mouse', 14.99, 150),
    (103, 'Monitor', 199.99, 50);

-- Updating Data 
-- Example: Update Sunita Smith's salary
UPDATE Employees
SET Salary = 58000
WHERE EmployeeID = 2;

-- Deleting Data 
-- Example: Remove Monitor from Products
DELETE FROM Products
WHERE ProductName = 'Monitor';

-- Querying Data 
-- Example: Select all employees
SELECT * FROM Employees;

-- Example: Select all products
SELECT * FROM Products;

-- Dropping Database (DDL)
-- Example: Drop CompanyDB
DROP DATABASE Company;
