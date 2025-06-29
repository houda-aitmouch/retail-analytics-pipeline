# 🛒 Retail Analytics Pipeline — Azure + Oracle-Compatible Tools

Built an end-to-end retail analytics pipeline using Python, Azure SQL, Oracle-style SQL queries, and a real-time dashboard powered by Streamlit.

---

## 💡 Objective

Simulate Oracle Analytics Cloud (OAC) experience using free, student-accessible cloud and open-source tools — suitable for Oracle PFE internship project.

---

## 🚀 Tech Stack

| Layer        | Technology                     |
|--------------|-------------------------------|
| Extract      | CSV → Python (Pandas)         |
| Transform    | Python (Pandas)               |
| Load         | Azure SQL (via `pyodbc`)      |
| Analytics    | Oracle-style SQL Queries      |
| Dashboard    | Streamlit (Oracle APEX-like)  |

---

## 📈 Dashboard Preview

![Dashboard Screenshot](dashboard/screenshot.png)

> Live KPIs for Revenue, Product Insights, and Customer Spending (Azure SQL + Streamlit)

---

## 📊 Sample Queries (Oracle-Compatible)

```sql
-- Total revenue by product
SELECT Product, SUM(Quantity * Price) AS Revenue
FROM RetailData
GROUP BY Product
ORDER BY Revenue DESC;

-- Top 5 customers
SELECT CustomerID, SUM(Quantity * Price) AS TotalSpent
FROM RetailData
GROUP BY CustomerID
ORDER BY TotalSpent DESC
FETCH FIRST 5 ROWS ONLY;# retail-analytics-pipeline
