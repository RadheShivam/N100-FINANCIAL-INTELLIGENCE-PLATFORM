import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

# Core files
companies = pd.read_excel("data/core/companies.xlsx", header=1)
profitandloss = pd.read_excel("data/core/profitandloss.xlsx", header=1)
balancesheet = pd.read_excel("data/core/balancesheet.xlsx", header=1)
cashflow = pd.read_excel("data/core/cashflow.xlsx", header=1)

# Supplementary files
financial_ratios = pd.read_excel("data/supplementary/financial_ratios.xlsx")
market_cap = pd.read_excel("data/supplementary/market_cap.xlsx")
peer_groups = pd.read_excel("data/supplementary/peer_groups.xlsx")
sectors = pd.read_excel("data/supplementary/sectors.xlsx")
stock_prices = pd.read_excel("data/supplementary/stock_prices.xlsx")

# Load data
companies.to_sql("companies", conn, if_exists="append", index=False)
profitandloss.to_sql("profitandloss", conn, if_exists="append", index=False)
balancesheet.to_sql("balancesheet", conn, if_exists="append", index=False)
cashflow.to_sql("cashflow", conn, if_exists="append", index=False)

financial_ratios.to_sql("financial_ratios", conn, if_exists="append", index=False)
market_cap.to_sql("market_cap", conn, if_exists="append", index=False)
peer_groups.to_sql("peer_groups", conn, if_exists="append", index=False)
sectors.to_sql("sectors", conn, if_exists="append", index=False)
stock_prices.to_sql("stock_prices", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("All datasets loaded successfully!")