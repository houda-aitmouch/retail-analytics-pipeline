import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"  # ✅ updated to 18
    f"Server={os.getenv('AZURE_SERVER')};"
    f"Database={os.getenv('AZURE_DB')};"
    f"Uid={os.getenv('AZURE_USER')};"
    f"Pwd={os.getenv('AZURE_PASSWORD')};"
    "Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"  # ✅ must be 'yes' or use CA cert
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Drop and create table
cursor.execute("""
IF OBJECT_ID('RetailData', 'U') IS NOT NULL DROP TABLE RetailData;
CREATE TABLE RetailData (
    InvoiceID VARCHAR(20),
    CustomerID VARCHAR(20),
    Product NVARCHAR(100),
    Quantity INT,
    Price FLOAT
)
""")
conn.commit()

# Load CSV and insert into SQL
df = pd.read_csv("data/retail_sample.csv")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO RetailData (InvoiceID, CustomerID, Product, Quantity, Price)
        VALUES (?, ?, ?, ?, ?)
    """, row.InvoiceID, row.CustomerID, row.Product, row.Quantity, row.Price)

conn.commit()
cursor.close()
conn.close()
print("✅ Retail data loaded to Azure SQL successfully.")