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

# DQ-04 Null Company ID Check
null_company = pd.read_sql("""
SELECT *
FROM profitandloss
WHERE company_id IS NULL
""", conn)

if len(null_company) > 0:
    failures.append(
        ["profitandloss", "DQ-04", "Null company_id"]
    )

# DQ-05 Null Year Check
null_year = pd.read_sql("""
SELECT *
FROM profitandloss
WHERE year IS NULL
""", conn)

if len(null_year) > 0:
    failures.append(
        ["profitandloss", "DQ-05", "Null year"]
    )

# DQ-06 Negative Market Cap Check

negative_market_cap = pd.read_sql("""
SELECT *
FROM market_cap
WHERE market_cap_crore < 0
""", conn)

if len(negative_market_cap) > 0:
    failures.append(
        ["market_cap", "DQ-06", "Negative market cap"]
    )

# DQ-07 Negative EPS Check

negative_eps = pd.read_sql("""
SELECT *
FROM profitandloss
WHERE eps < 0
""", conn)

print(
    f"WARNING: {len(negative_eps)} records have negative EPS"
)

# DQ-08 Invalid ROE Check

invalid_roe = pd.read_sql("""
SELECT *
FROM companies
WHERE roe_percentage < -100
OR roe_percentage > 100
""", conn)

print(
    f"WARNING: {len(invalid_roe)} records have ROE outside expected range"
)


# DQ-09 ROCE Validation

invalid_roce = pd.read_sql("""
SELECT *
FROM companies
WHERE roce_percentage < -100
OR roce_percentage > 100
""", conn)

print(
    f"WARNING: {len(invalid_roce)} records have ROCE outside expected range"
)

# DQ-10 Missing Stock Prices

missing_prices = pd.read_sql("""
SELECT *
FROM stock_prices
WHERE close_price IS NULL
""", conn)

if len(missing_prices) > 0:
    failures.append(
        ["stock_prices", "DQ-10", "Missing close price"]
    )

# DQ-11 Duplicate Company Names

duplicate_names = pd.read_sql("""
SELECT company_name, COUNT(*)
FROM companies
GROUP BY company_name
HAVING COUNT(*) > 1
""", conn)

if len(duplicate_names) > 0:
    failures.append(
        ["companies", "DQ-11", "Duplicate company names"]
    )

# DQ-13 Future Dates

future_dates = pd.read_sql("""
SELECT *
FROM stock_prices
WHERE date > DATE('now')
""", conn)

if len(future_dates) > 0:
    failures.append(
        ["stock_prices", "DQ-13", "Future dates found"]
    )

# DQ-14 Missing Peer Groups

missing_peers = pd.read_sql("""
SELECT *
FROM peer_groups
WHERE peer_group_name IS NULL
""", conn)

if len(missing_peers) > 0:
    failures.append(
        ["peer_groups", "DQ-14", "Missing peer group"]
    )

# DQ-15 Negative Volume

negative_volume = pd.read_sql("""
SELECT *
FROM stock_prices
WHERE volume < 0
""", conn)

if len(negative_volume) > 0:
    failures.append(
        ["stock_prices", "DQ-15", "Negative volume"]
    )

# DQ-16 Orphan Foreign Keys

orphan_records = pd.read_sql("""
SELECT p.*
FROM profitandloss p
LEFT JOIN companies c
ON p.company_id = c.id
WHERE c.id IS NULL
""", conn)

print(
    f"WARNING: {len(orphan_records)} orphan foreign key records found"
)

# Create Validation Report
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