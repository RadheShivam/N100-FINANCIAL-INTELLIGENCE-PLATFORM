import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    COUNT(DISTINCT year) AS total_years
FROM profitandloss
GROUP BY company_id
ORDER BY total_years ASC
""", conn)

print(df)

conn.close()