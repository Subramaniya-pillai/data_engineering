
-- SQL ASSIGNMENT – Product Inventory Management

-- 1. Create Database and Use It
CREATE DATABASE ProductManagementDB;
USE ProductManagementDB;

-- 2. Create ProductInventory Table
CREATE TABLE ProductInventory (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    Supplier VARCHAR(100),
    LastRestocked DATE
);

-- 3. Insert Sample Data
INSERT INTO ProductInventory (ProductID, ProductName, Category, Quantity, UnitPrice, Supplier, LastRestocked)
VALUES
(1, 'Laptop', 'Electronics', 20, 70000, 'TechMart', '2025-04-20'),
(2, 'Office Chair', 'Furniture', 50, 5000, 'HomeComfort', '2025-04-18'),
(3, 'Smartwatch', 'Electronics', 30, 15000, 'GadgetHub', '2025-04-22'),
(4, 'Desk Lamp', 'Lighting', 80, 1200, 'BrightLife', '2025-04-25'),
(5, 'Wireless Mouse', 'Electronics', 100, 1500, 'GadgetHub', '2025-04-30');

-- 4. CRUD Operations

-- Add New Product
INSERT INTO ProductInventory VALUES
(6, 'Gaming Keyboard', 'Electronics', 40, 3500, 'TechMart', '2025-05-01');

-- Update Quantity of Desk Lamp
UPDATE ProductInventory
SET Quantity = Quantity + 20
WHERE ProductName = 'Desk Lamp';

-- Delete Office Chair
DELETE FROM ProductInventory
WHERE ProductID = 2;

-- Display All Products Sorted by ProductName
SELECT * FROM ProductInventory
ORDER BY ProductName ASC;

-- 5. Sorting and Filtering

-- Sort by Quantity (Descending)
SELECT * FROM ProductInventory
ORDER BY Quantity DESC;

-- Filter by Category: Electronics
SELECT * FROM ProductInventory
WHERE Category = 'Electronics';

-- AND Condition: Electronics with Quantity > 20
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' AND Quantity > 20;

-- OR Condition: Electronics or UnitPrice < 2000
SELECT * FROM ProductInventory
WHERE Category = 'Electronics' OR UnitPrice < 2000;

-- 6. Aggregation and Grouping

-- Total Stock Value (Quantity × UnitPrice)
SELECT SUM(Quantity * UnitPrice) AS TotalStockValue
FROM ProductInventory;

-- Average UnitPrice by Category
SELECT Category, AVG(UnitPrice) AS AveragePrice
FROM ProductInventory
GROUP BY Category;

-- Count of Products Supplied by GadgetHub
SELECT COUNT(*) AS ProductCount
FROM ProductInventory
WHERE Supplier = 'GadgetHub';

-- 7. Conditional & Pattern Matching

-- ProductName Starting with 'W'
SELECT * FROM ProductInventory
WHERE ProductName LIKE 'W%';

-- GadgetHub Products with UnitPrice > 10000
SELECT * FROM ProductInventory
WHERE Supplier = 'GadgetHub' AND UnitPrice > 10000;

-- UnitPrice BETWEEN 1000 AND 20000
SELECT * FROM ProductInventory
WHERE UnitPrice BETWEEN 1000 AND 20000;

-- 8. Advanced Queries

-- Top 3 Most Expensive Products
SELECT * FROM ProductInventory
ORDER BY UnitPrice DESC
LIMIT 3;

-- Products Restocked in Last 10 Days
SELECT * FROM ProductInventory
WHERE LastRestocked >= DATE_SUB(CURDATE(), INTERVAL 10 DAY);

-- Total Quantity per Supplier
SELECT Supplier, SUM(Quantity) AS TotalQuantity
FROM ProductInventory
GROUP BY Supplier;

-- Products with Quantity < 30
SELECT * FROM ProductInventory
WHERE Quantity < 30;

-- 9. Joins & Subqueries

-- Supplier with Most Products
SELECT Supplier, COUNT(*) AS ProductCount
FROM ProductInventory
GROUP BY Supplier
ORDER BY ProductCount DESC
LIMIT 1;

-- Product with Highest Stock Value (Quantity × UnitPrice)
SELECT ProductID, ProductName, Quantity, UnitPrice,
       (Quantity * UnitPrice) AS StockValue
FROM ProductInventory
ORDER BY StockValue DESC
LIMIT 1;
