-- E-commerce Sales Analytics - MySQL
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

CREATE TABLE IF NOT EXISTS ecommerce_sales (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR(10),
    City VARCHAR(50),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Discount_Percent INT,
    Sales DECIMAL(12,2),
    Payment_Method VARCHAR(30),
    Order_Status VARCHAR(30)
);

-- Import ecommerce_sales.csv using MySQL Workbench:
-- Table Data Import Wizard -> select this table -> map matching columns.

-- 1. Total orders and sales
SELECT COUNT(*) AS total_orders, SUM(Sales) AS total_sales
FROM ecommerce_sales;

-- 2. Average order value
SELECT ROUND(AVG(Sales),2) AS average_order_value
FROM ecommerce_sales;

-- 3. Monthly sales
SELECT DATE_FORMAT(Order_Date,'%Y-%m') AS month, SUM(Sales) AS monthly_sales
FROM ecommerce_sales
GROUP BY DATE_FORMAT(Order_Date,'%Y-%m')
ORDER BY month;

-- 4. Sales by category
SELECT Category, SUM(Sales) AS total_sales
FROM ecommerce_sales
GROUP BY Category ORDER BY total_sales DESC;

-- 5. Top five products
SELECT Product, SUM(Sales) AS total_sales
FROM ecommerce_sales
GROUP BY Product ORDER BY total_sales DESC LIMIT 5;

-- 6. Orders by payment method
SELECT Payment_Method, COUNT(*) AS total_orders
FROM ecommerce_sales
GROUP BY Payment_Method ORDER BY total_orders DESC;

-- 7. Orders by status
SELECT Order_Status, COUNT(*) AS total_orders
FROM ecommerce_sales
GROUP BY Order_Status ORDER BY total_orders DESC;

-- 8. City-wise sales
SELECT City, SUM(Sales) AS total_sales
FROM ecommerce_sales
GROUP BY City ORDER BY total_sales DESC;
