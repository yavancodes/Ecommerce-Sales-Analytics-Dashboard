# E-commerce Sales Analysis - beginner-friendly Python code
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Total Orders:", df["Order_ID"].nunique())
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Average Order Value:", round(df["Sales"].mean(), 2))
print("Total Quantity Sold:", df["Quantity"].sum())

# Chart 1: Monthly sales
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Revenue")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.tight_layout()
plt.savefig("01_monthly_sales.png"); plt.show()

# Chart 2: Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category"); plt.ylabel("Sales"); plt.tight_layout()
plt.savefig("02_category_sales.png"); plt.show()

# Chart 3: Top five products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
top_products.plot(kind="bar", title="Top 5 Products by Sales")
plt.xlabel("Product"); plt.ylabel("Sales"); plt.tight_layout()
plt.savefig("03_top_products.png"); plt.show()

# Chart 4: Payment method
payment_counts = df["Payment_Method"].value_counts()
payment_counts.plot(kind="bar", title="Orders by Payment Method")
plt.xlabel("Payment Method"); plt.ylabel("Orders"); plt.tight_layout()
plt.savefig("04_payment_methods.png"); plt.show()

# Chart 5: Order status
status_counts = df["Order_Status"].value_counts()
status_counts.plot(kind="bar", title="Orders by Status")
plt.xlabel("Order Status"); plt.ylabel("Orders"); plt.tight_layout()
plt.savefig("05_order_status.png"); plt.show()

# Chart 6: Monthly order count
monthly_orders = df.groupby(df["Order_Date"].dt.to_period("M"))["Order_ID"].nunique()
monthly_orders.plot(kind="line", marker="o", title="Monthly Number of Orders")
plt.xlabel("Month"); plt.ylabel("Orders"); plt.tight_layout()
plt.savefig("06_monthly_orders.png"); plt.show()
