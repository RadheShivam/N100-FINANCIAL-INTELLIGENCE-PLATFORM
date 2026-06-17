import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "sectors",
    "stock_prices"
]

rows = []

for table in tables:

    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table}")

    count = cur.fetchone()[0]

    rows.append([
        table,
        count,
        0,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

audit_df = pd.DataFrame(
    rows,
    columns=[
        "table_name",
        "rows_loaded",
        "rows_rejected",
        "timestamp"
    ]
)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print("load_audit.csv created successfully!")

conn.close()