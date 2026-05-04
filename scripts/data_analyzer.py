# kaggle dataset link:
# https://www.kaggle.com/datasets/rohitgrewal/restaurant-sales-data

import numpy as np
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_CSV = ROOT / "data" / "raw" / "sales" / "9. Sales-Data-Analysis.csv"
OUT_CSV = ROOT / "data" / "processed" / "analyzed_sales.csv"

df = pd.read_csv(RAW_CSV)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

dateDT = df["Date"].dtype
print(dateDT)
print(df.info())

df["Amount"] = df["Quantity"] * df["Price"]
print(df[["Amount", "Quantity", "Price"]].head())

dfSampleIndices = df.sample(frac=0.05).index
df.loc[dfSampleIndices, "Amount"] = np.nan
df["Amount"] = df["Amount"].fillna(df["Amount"].mean())

df["Profit_Margin"] = df["Amount"] * 0.15

rates_data = {
    "City": ["London", "Madrid", "Lisbon", "Berlin", "Paris"],
    "Conversion_Factor": [1.25, 1.08, 1.08, 1.08, 1.08],
}
df_rates = pd.DataFrame(rates_data)
df = pd.merge(df, df_rates, on="City", how="left")

df["USD_Amount"] = df["Amount"] * df["Conversion_Factor"]

city_sales = df.groupby("City")["Amount"].sum()
print(f"Total Sales per City:\n{city_sales.to_string(header=False, name=False)}")

monthly_margin = df.groupby(pd.Grouper(key="Date", freq="ME"))["Profit_Margin"].mean()
print(f"Average Profit Margin per Month:\n{monthly_margin}")

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_CSV, index=False)
