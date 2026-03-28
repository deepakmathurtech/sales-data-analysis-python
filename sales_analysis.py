import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("product_sales_dataset_final.csv")
df.columns = df.columns.str.strip()

print("dataset loaded")
print(df.shape)

print("\nfirst few rows")
print(df.head())

print("\ninfo")
df.info()

print("\nsummary stats")
print(df.describe())

print("\nmissing values")
print(df.isnull().sum())

df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%m-%d-%y")
df["Month"] = df["Order_Date"].dt.month

total_rev = df["Revenue"].sum()
total_profit = df["Profit"].sum()
avg_profit = df["Profit"].mean()

print("\ntotal revenue:", total_rev)
print("total profit:", total_profit)
print("average profit:", avg_profit)

cat_sales = df.groupby("Category")["Revenue"].sum()

plt.figure()
cat_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure()
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.show()

monthly_rev = df.groupby("Month")["Revenue"].sum()

plt.figure()
monthly_rev.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

top_products = (
    df.groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.hist(df["Quantity"], bins=20)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure()
plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%")
plt.title("Sales by Region")
plt.show()

top_customers = (
    df.groupby("Customer_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop customers by revenue")
print(top_customers)

df.to_csv("processed_sales_data.csv", index=False)

print("\nprocessed file saved")
