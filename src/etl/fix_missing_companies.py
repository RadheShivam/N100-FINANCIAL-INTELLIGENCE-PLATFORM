import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

missing_companies = [
    ("ULTRACEMCO", "UltraTech Cement Ltd"),
    ("UNIONBANK", "Union Bank of India"),
    ("UNITDSPR", "United Spirits Ltd"),
    ("VBL", "Varun Beverages Ltd"),
    ("VEDL", "Vedanta Ltd"),
    ("WIPRO", "Wipro Ltd"),
    ("ZOMATO", "Zomato Ltd"),
    ("ZYDUSLIFE", "Zydus Lifesciences Ltd")
]

for company_id, company_name in missing_companies:

    cursor.execute("""
    INSERT OR IGNORE INTO companies (
        id,
        company_name
    )
    VALUES (?, ?)
    """, (company_id, company_name))

conn.commit()
conn.close()

print("Missing companies inserted successfully!")