import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql("""
SELECT
    company_id,
    COUNT(DISTINCT year) AS years_available
FROM profitandloss
GROUP BY company_id
HAVING COUNT(DISTINCT year) < 5
ORDER BY years_available
""", conn)

print(df)

conn.close()