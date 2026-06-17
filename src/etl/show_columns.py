import pandas as pd

files = [
    "data/core/companies.xlsx",
    "data/core/profitandloss.xlsx",
    "data/core/balancesheet.xlsx",
    "data/core/cashflow.xlsx"
]

for file in files:
    print("\n" + "="*80)
    print(file)
    print("="*80)

    df = pd.read_excel(file, header=1)

    print(df.columns.tolist())