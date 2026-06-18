# src/etl/fix_agtl.py

import sqlite3

conn = sqlite3.connect("nifty100.db")

cursor = conn.cursor()

cursor.execute("""
INSERT OR IGNORE INTO companies
(id, company_name)
VALUES
('AGTL', 'Adani Green Energy Ltd')
""")

conn.commit()
conn.close()

print("AGTL inserted successfully!")