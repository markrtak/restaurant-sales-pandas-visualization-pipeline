# E-commerce sales pipeline

Restaurant sales feature engineering with NumPy and Pandas and interactive e-commerce trend reporting.

Two-step workflow: enrich restaurant sales CSV with NumPy/Pandas, then visualize trends and correlations (Matplotlib/Seaborn/Plotly).

Repository: [markrtak/restaurant-sales-pandas-visualization-pipeline](https://github.com/markrtak/restaurant-sales-pandas-visualization-pipeline)

## Layout

| Path | Purpose |
|------|---------|
| `data/raw/sales/9. Sales-Data-Analysis.csv` | Source dataset (restaurant sales). |
| `data/processed/analyzed_sales.csv` | Written by `data_analyzer.py` — run analyzer to regenerate. |
| `scripts/data_analyzer.py` | Transformations (amounts, profit margin, FX to USD, etc.). |
| `scripts/visualization_report.py` | Plots + interactive Scatter HTML output. |
| `outputs/` | Created when you run the visualization script (`*.png`, `interactive_scatter.html`). |

Dataset reference: [Restaurant sales – Kaggle](https://www.kaggle.com/datasets/rohitgrewal/restaurant-sales-data).

## Prerequisites

```bash
pip install pandas numpy matplotlib seaborn plotly
```

## Usage

Run from project root (`ecommerce-sales-pipeline`).

### 1. Produce processed data

```bash
python scripts/data_analyzer.py
```

Updates `data/processed/analyzed_sales.csv`.

### 2. Charts and Plotly HTML

```bash
python scripts/visualization_report.py
```

Artifacts appear under `outputs/` (figures may display in a browser depending on Plotly renderer settings).
