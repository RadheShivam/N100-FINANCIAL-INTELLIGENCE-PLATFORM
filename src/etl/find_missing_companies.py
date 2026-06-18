# src/etl/find_missing_companies.py

import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql("""
SELECT DISTINCT company_id
FROM profitandloss
WHERE company_id NOT IN (
    SELECT id
    FROM companies
)
ORDER BY company_id
""", conn)

print(df)

conn.close()