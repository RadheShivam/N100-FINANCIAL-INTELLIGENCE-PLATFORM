# validator.py
import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

failures = []

# DQ-01 Primary Key Check
tables = [
    ("companies", "id"),
    ("profitandloss", "id"),
    ("balancesheet", "id"),
    ("cashflow", "id"),
    ("financial_ratios", "id"),
    ("market_cap", "id"),
    ("peer_groups", "id"),
    ("sectors", "id"),
    ("stock_prices", "id")
]

for table, pk in tables:

    query = f"""
    SELECT {pk}, COUNT(*)
    FROM {table}
    GROUP BY {pk}
    HAVING COUNT(*) > 1
    """

    duplicates = pd.read_sql(query, conn)

    if len(duplicates) > 0:
        failures.append(
            [table, "DQ-01", "Duplicate Primary Key"]
        )

# DQ-02 Sales Positive
sales_check = pd.read_sql("""
SELECT *
FROM profitandloss
WHERE sales <= 0
""", conn)

if len(sales_check) > 0:
    failures.append(
        ["profitandloss", "DQ-02", "Non-positive sales"]
    )

# DQ-03 Assets = Liabilities Check
balance_check = pd.read_sql("""
SELECT *
FROM balancesheet
WHERE ABS(total_assets-total_liabilities) > 1000
""", conn)

if len(balance_check) > 0:
    failures.append(
        ["balancesheet", "DQ-03", "Asset mismatch"]
    )

fail_df = pd.DataFrame(
    failures,
    columns=[
        "table_name",
        "rule_id",
        "description"
    ]
)

fail_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("\nValidation Complete")

print(f"\nFailures Found: {len(fail_df)}")

conn.close()