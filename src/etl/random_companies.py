import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql("""
SELECT
    id,
    company_name
FROM companies
ORDER BY RANDOM()
LIMIT 5
""", conn)

print(df)

conn.close()