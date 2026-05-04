# E-commerce sales pipeline

Restaurant sales feature engineering with NumPy and Pandas and interactive e-commerce trend reporting.

Workflow: enrich a restaurant sales CSV, then visualize trends and correlations with Matplotlib, Seaborn, and Plotly.

<p><img src="https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/><img src="https://img.shields.io/badge/PANDAS-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/><img src="https://img.shields.io/badge/NUMPY-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/><img src="https://img.shields.io/badge/MATPLOTLIB-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/><img src="https://img.shields.io/badge/SEABORN-9C554A?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn"/><img src="https://img.shields.io/badge/PLOTLY-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/></p>

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
