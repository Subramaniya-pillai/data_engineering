-- Create Database
CREATE DATABASE BookStoreDB;
USE BookStoreDB;

-- Create Book Table
CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50),
    Price DECIMAL(10, 2),
    PublishedYear INT,
    Stock INT
);

-- Insert Initial Data
INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock) VALUES
(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300.00, 1988, 50),
(2, 'Sapiens', 'Yuval Noah Harari', 'Non-Fiction', 500.00, 2011, 30),
(3, 'Atomic Habits', 'James Clear', 'Self-Help', 400.00, 2018, 25),
(4, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Personal Finance', 350.00, 1997, 20),
(5, 'The Lean Startup', 'Eric Ries', 'Business', 450.00, 2011, 15);

-- 1. CRUD OPERATIONS

-- Add a new book
INSERT INTO Book (BookID, Title, Author, Genre, Price, PublishedYear, Stock)
VALUES (6, 'Deep Work', 'Cal Newport', 'Self-Help', 420.00, 2016, 35);

-- Update price: Increase price of all Self-Help books by 50
UPDATE Book
SET Price = Price + 50
WHERE Genre = 'Self-Help';

-- Delete a book with BookID = 4
DELETE FROM Book
WHERE BookID = 4;

-- Read all books sorted by Title (ascending)
SELECT * FROM Book
ORDER BY Title ASC;

-- 2. SORTING AND FILTERING

-- Sort books by price (descending)
SELECT * FROM Book
ORDER BY Price DESC;

-- Filter: Books in Fiction genre
SELECT * FROM Book
WHERE Genre = 'Fiction';

-- Filter with AND: Self-Help books priced above 400
SELECT * FROM Book
WHERE Genre = 'Self-Help' AND Price > 400;

-- Filter with OR: Fiction books OR published after 2000
SELECT * FROM Book
WHERE Genre = 'Fiction' OR PublishedYear > 2000;

-- 3. AGGREGATION AND GROUPING

-- Total stock value = SUM(Price * Stock)
SELECT SUM(Price * Stock) AS TotalStockValue
FROM Book;

-- Average book price by Genre
SELECT Genre, AVG(Price) AS AveragePrice
FROM Book
GROUP BY Genre;

-- Total books by author: Paulo Coelho
SELECT COUNT(*) AS TotalBooksByCoelho
FROM Book
WHERE Author = 'Paulo Coelho';

-- 4. CONDITIONAL AND PATTERN MATCHING

-- Titles containing the word "The"
SELECT * FROM Book
WHERE Title LIKE '%The%';

-- Books by Yuval Noah Harari priced below 600
SELECT * FROM Book
WHERE Author = 'Yuval Noah Harari' AND Price < 600;

-- Books priced between 300 and 500
SELECT * FROM Book
WHERE Price BETWEEN 300 AND 500;

-- 5. ADVANCED QUERIES

-- Top 3 most expensive books
SELECT * FROM Book
ORDER BY Price DESC
LIMIT 3;

-- Books published before the year 2000
SELECT * FROM Book
WHERE PublishedYear < 2000;

-- Count total books in each Genre
SELECT Genre, COUNT(*) AS TotalBooks
FROM Book
GROUP BY Genre;

-- Find duplicate titles
SELECT Title, COUNT(*) AS Count
FROM Book
GROUP BY Title
HAVING COUNT(*) > 1;

-- 6. SUBQUERIES AND GROUPED RESULTS

-- Author with the most books
SELECT Author, COUNT(*) AS BookCount
FROM Book
GROUP BY Author
ORDER BY BookCount DESC
LIMIT 1;

-- Oldest book by each Genre
SELECT Genre, Title, Author, PublishedYear
FROM Book b
WHERE PublishedYear = (
    SELECT MIN(PublishedYear)
    FROM Book
    WHERE Genre = b.Genre
);
