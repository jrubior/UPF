"""Reproduce the synthetic school dataset and OLS results for Lecture 4 v3.

Run with Python 3, NumPy and SciPy. No real school or student records are used.
Seed and generating parameters are fixed; saved CSV values drive all results.
"""
from pathlib import Path
import csv
import json
import random
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "lecture4v3"
rng = random.Random(251174)
rows = []
for i in range(1, 101):
    x = round(rng.uniform(16, 28), 1)
    v = rng.uniform(-10, 10)
    z = round(70 - 1.5 * x + v, 2)
    epsilon = round(rng.gauss(0, 10), 4)
    u = 1.5 * (z - 40) + epsilon
    y = round(700 - 2 * x + u, 4)
    rows.append([i, y, x, z])
with (OUT / "school_data.csv").open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["school_id", "Y_score", "X_class_size", "Z_income_kEUR"])
    writer.writerows(rows)

a = np.array(rows)
y, x, z = a[:, 1], a[:, 2], a[:, 3]
def ols(design):
    beta = np.linalg.lstsq(design, y, rcond=None)[0]
    residuals = y - design @ beta
    n, k = design.shape
    ssr = residuals @ residuals
    sst = np.sum((y - y.mean()) ** 2)
    se = np.sqrt(np.diag(ssr / (n - k) * np.linalg.inv(design.T @ design)))
    t = beta / se
    p = 2 * stats.t.sf(np.abs(t), n - k)
    critical = stats.t.ppf(.975, n - k)
    return dict(beta=beta.tolist(), se=se.tolist(), t=t.tolist(), p=p.tolist(),
                ci=np.column_stack([beta-critical*se, beta+critical*se]).tolist(),
                ssr=float(ssr), sst=float(sst), r2=float(1-ssr/sst),
                adj_r2=float(1-(ssr/(n-k))/(sst/(n-1))),
                ser=float(np.sqrt(ssr/(n-k))), rmse=float(np.sqrt(ssr/n)),
                df=n-k, critical=float(critical))
simple = ols(np.column_stack([np.ones(100), x]))
multiple = ols(np.column_stack([np.ones(100), x, z]))
summary = dict(seed=251174, n=100, simple=simple, multiple=multiple,
               corr_xz=float(np.corrcoef(x,z)[0,1]),
               mean=[float(v.mean()) for v in [y,x,z]],
               sd=[float(v.std(ddof=1)) for v in [y,x,z]],
               minimum=[float(v.min()) for v in [y,x,z]],
               maximum=[float(v.max()) for v in [y,x,z]],
               rows=rows,
               slope_zx=float(np.cov(x,z,ddof=1)[0,1]/np.var(x,ddof=1)))
(OUT / "results.json").write_text(json.dumps(summary, indent=2) + "\n")

print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2))
