# Dynamic Hotel Overbooking Optimization

A data-driven approach to hotel overbooking optimization using cancellation prediction and stochastic optimization. The project is split into three stages: exploratory analysis, cancellation prediction, and overbooking policy optimization.

---

## Project Structure

```
hotel-overbook/
├── data/                   # Raw and processed datasets
├── outputs/                # Generated plots and result files
├── 00_data_stat.ipynb      # Exploratory data analysis & statistics
├── part1_pred.ipynb        # Cancellation prediction models
├── part2_optim.ipynb       # Overbooking optimization
├── part3_analysis.ipynb    # Results analysis and interpretation
├── utils.py                # Shared helper functions
├── download_data.py        # Script to download dataset via kagglehub
└── requirements.txt        # Python dependencies
```

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/leo-leung04/hotel-overbook.git
cd hotel-overbook
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebooks in order

Open and run the notebooks in this order:

1. `00_data_stat.ipynb` — data overview and feature exploration
2. `part1_pred.ipynb` — train cancellation prediction models (XGBoost, etc.)
3. `part2_optim.ipynb` — use predictions to optimize overbooking policy
4. `part3_analysis.ipynb` — evaluate results and visualize outcomes

---

## Dependencies

| Package | Purpose |
|---|---|
| `pandas` | Data manipulation |
| `numpy` | Numerical computing |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualization |
| `scikit-learn` | Machine learning utilities |
| `xgboost` | Gradient boosting classifier |
| `kagglehub` | Dataset download from Kaggle |


---

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab to open the notebooks

---

## Notes

- All notebooks depend on `utils.py` for shared functions — do not move or rename it
- Outputs (plots, CSVs) are saved to the `outputs/` directory