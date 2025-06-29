import streamlit as st
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# SQL connection string
conn_str = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={os.getenv('AZURE_SERVER')};"
    f"Database={os.getenv('AZURE_DB')};"
    f"Uid={os.getenv('AZURE_USER')};"
    f"Pwd={os.getenv('AZURE_PASSWORD')};"
    "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
)

# Connect to Azure SQL
conn = pyodbc.connect(conn_str)

# Load retail data into a DataFrame
df = pd.read_sql("SELECT * FROM RetailData", conn)

# Streamlit UI
st.title("Retail Analytics Dashboard")
st.markdown("Powered by Azure SQL + Streamlit")

# KPI: Total Revenue
total_revenue = (df["Quantity"] * df["Price"]).sum()
st.metric("Total Revenue", f"${total_revenue:,.2f}")

# Revenue by Product
st.subheader("Revenue by Product")
revenue_product = df.groupby("Product").apply(lambda x: (x["Quantity"] * x["Price"]).sum())
st.bar_chart(revenue_product.sort_values(ascending=False))

# Top Customers
st.subheader("Top 5 Customers by Spending")
top_customers = df.groupby("CustomerID").apply(lambda x: (x["Quantity"] * x["Price"]).sum()).sort_values(ascending=False).head(5)
st.dataframe(top_customers.reset_index(name="TotalSpent"))

# Table Preview
st.subheader("Sample Transactions")
st.dataframe(df.head(20))

# Close connection
conn.close()