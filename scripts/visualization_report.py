from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.io as pio
import seaborn as sns

pio.renderers.default = "browser"

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "outputs"
DATA_CSV = ROOT / "data" / "processed" / "analyzed_sales.csv"

OUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_CSV)
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")

plt.plot(df["Date"], df["USD_Amount"])
plt.xlabel("Time")
plt.ylabel("USD Amount")
plt.title("Monthly Sales Trend (USD_Amount)")
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.gcf().autofmt_xdate()
plt.savefig(OUT_DIR / "sales_trend.png")
plt.show()

sns.heatmap(
    df[
        ["Price", "Quantity", "Amount", "Profit_Margin", "Conversion_Factor", "USD_Amount"]
    ].corr(),
    annot=True,
    cmap="RdBu",
)
plt.title("Correlation Matrix of Sales Metrics")
plt.savefig(OUT_DIR / "correlation_matrix.png")
plt.show()

fig = px.scatter(
    df,
    x="USD_Amount",
    y="Profit_Margin",
    color="City",
    hover_data="Order ID",
    title="Profit Margin vs. USD Amount by Region",
    labels={
        "USD_Amount": "Amount (USD)",
        "Profit_Margin": "Profit Margin (%)",
    },
)
fig.update_traces(marker=dict(size=10, opacity=0.7))
fig.show()
fig.write_html(OUT_DIR / "interactive_scatter.html")
