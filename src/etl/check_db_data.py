# src/etl/check_db_data.py

import sqlite3

conn = sqlite3.connect("nifty100.db")

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM companies")
print("companies:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM profitandloss")
print("profitandloss:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM balancesheet")
print("balancesheet:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM cashflow")
print("cashflow:", cur.fetchone()[0])

conn.close()