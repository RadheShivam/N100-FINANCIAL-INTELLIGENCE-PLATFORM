import sqlite3

conn = sqlite3.connect("nifty100.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM financial_ratios")
print("financial_ratios:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM market_cap")
print("market_cap:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM peer_groups")
print("peer_groups:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM sectors")
print("sectors:", cur.fetchone()[0])

cur.execute("SELECT COUNT(*) FROM stock_prices")
print("stock_prices:", cur.fetchone()[0])

conn.close()