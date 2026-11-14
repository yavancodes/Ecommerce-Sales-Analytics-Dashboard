# Ecommerce-Sales-Analytics-Dashboard
Project Overview
A simple beginner-level project that analyzes 120 sample e-commerce orders using Python, MySQL, Excel and CSV.
Project Files
- ecommerce_sales.csv - dataset with 120 orders
- ecommerce_sales.xlsx - Excel workbook with Sales Data and Summary sheets
- ecommerce_sales_analysis.py - Python analysis and six charts
- ecommerce_sales_analysis.sql - MySQL table and analysis queries
- charts/ - six chart images
- requirements.txt - Python libraries
Dataset Columns
Order_ID, Order_Date, Customer_ID, City, Product, Category, Quantity, Unit_Price, Discount_Percent, Sales, Payment_Method, Order_Status.
Tools
Python (pandas, matplotlib), MySQL, Excel and CSV.
Run the Python Project
1. Install Python.
2. Put the Python file and CSV file in the same folder.
3. Open terminal in that folder.
4. Install libraries: pip install -r requirements.txt
5. Run: python ecommerce_sales_analysis.py
The script prints summary numbers and displays/saves six charts.
Run the SQL Project
1. Open MySQL Workbench.
2. Open and run ecommerce_sales_analysis.sql.
3. Import ecommerce_sales.csv into the ecommerce_sales table with Table Data Import Wizard.
4. Run the SELECT queries.
Six Charts
1. Monthly Sales Revenue
2. Sales by Category
3. Top 5 Products by Sales
4. Orders by Payment Method
5. Orders by Status
6. Monthly Number of Orders
Business Questions
- What are total sales and total orders?
- Which month had the highest sales?
- Which category generated the most revenue?
- Which five products generated the most sales?
- Which payment method is most common?
- What is the order-status breakdown?
- Which city generated the most sales?
Note
The dataset is generated for learning and portfolio practice. It is not real company data.
Sales = Unit_Price x Quantity after applying the discount.
