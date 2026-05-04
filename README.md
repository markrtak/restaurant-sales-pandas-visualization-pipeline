# E-commerce sales pipeline

Restaurant sales feature engineering with NumPy and Pandas and interactive e-commerce trend reporting.

Workflow: enrich a restaurant sales CSV, then visualize trends and correlations with Matplotlib, Seaborn, and Plotly.

<p align="left">
  <img src="https://skillicons.dev/icons?i=py,pandas,numpy,matplotlib,seaborn,plotly" height="48" alt="Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly" />
</p>

Repository: [markrtak/restaurant-sales-pandas-visualization-pipeline](https://github.com/markrtak/restaurant-sales-pandas-visualization-pipeline)

## Layout

| Path | Purpose |
|------|---------|
| `data/raw/sales/9. Sales-Data-Analysis.csv` | Source dataset (restaurant sales). |
| `data/processed/analyzed_sales.csv` | Written by `data_analyzer.py` — run analyzer to regenerate. |
| `scripts/data_analyzer.py` | Transformations (amounts, profit margin, FX to USD, etc.). |
| `scripts/visualization_report.py` | Plots + interactive Scatter HTML output. |
| `outputs/` | Created when you run the visualization script (`*.png`, `interactive_scatter.html`). |

Dataset: [Restaurant sales – Kaggle](https://www.kaggle.com/datasets/rohitgrewal/restaurant-sales-data).

## Prerequisites

```bash
pip install pandas numpy matplotlib seaborn plotly
```

## Usage

Run from the project root.

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
