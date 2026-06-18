# src/etl/check_cashflow_orphans.py

import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

df = pd.read_sql("""
SELECT *
FROM cashflow
WHERE id BETWEEN 189 AND 195
""", conn)

print(df)

conn.close()