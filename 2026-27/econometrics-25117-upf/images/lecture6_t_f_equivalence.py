"""Draw the q=1 rejection regions used in Lecture 6 (large-sample limit)."""
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, norm

blue = "#0072B2"
red = "#D55E00"
critical_t = norm.ppf(0.975)
critical_f = chi2.ppf(0.95, 1)
assert np.isclose(critical_t**2, critical_f)
assert np.isclose(2 * norm.sf(critical_t), chi2.sf(critical_f, 1))

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "pdf.fonttype": 42, "axes.spines.top": False,
                     "axes.spines.right": False})
fig, (ax_t, ax_f) = plt.subplots(1, 2, figsize=(12, 3.2))
fig.subplots_adjust(left=0.045, right=0.99, bottom=0.20, top=0.80, wspace=0.26)

x = np.linspace(-3.8, 3.8, 1600)
ax_t.plot(x, norm.pdf(x), color=blue, lw=2)
for lo, hi in [(-3.8, -critical_t), (critical_t, 3.8)]:
    tail = np.linspace(lo, hi, 400)
    ax_t.fill_between(tail, norm.pdf(tail), color=red, alpha=0.6)
for c in [-critical_t, critical_t]:
    ax_t.vlines(c, 0, norm.pdf(c), color=red, ls="--", lw=1.2)
ax_t.set(xlim=(-3.8, 3.8), ylim=(0, 0.44), yticks=[],
         xticks=[-critical_t, 0, critical_t],
         xticklabels=[r"$-1.96$", "0", r"$+1.96$"], xlabel=r"$t$")
ax_t.set_title("Two-sided t-test\n" + r"Large-sample limit: $N(0,1)$", fontsize=13)
for sign in [-1, 1]:
    ax_t.annotate(r"$2.5\%$", xy=(sign * 2.4, 0.015),
                  xytext=(sign * 2.9, 0.13), ha="center", color=red,
                  arrowprops={"arrowstyle": "->", "color": red})

x = np.linspace(0.001, 8, 2000)
ax_f.plot(x, chi2.pdf(x, 1), color=blue, lw=2)
tail = np.linspace(critical_f, 8, 600)
ax_f.fill_between(tail, chi2.pdf(tail, 1), color=red, alpha=0.6)
ax_f.vlines(critical_f, 0, chi2.pdf(critical_f, 1), color=red, ls="--", lw=1.2)
ax_f.set(xlim=(0, 8), ylim=(0, 0.65), yticks=[],
         xticks=[0, critical_f], xticklabels=["0", r"$3.84$"], xlabel=r"$F=t^2$")
ax_f.set_title("Right-tail F-test\n" + r"$q=1$: $F_{1,\infty}=\chi^2_1$", fontsize=13)
ax_f.annotate(r"$5\%$", xy=(4.7, 0.008), xytext=(5.3, 0.20),
              ha="center", color=red,
              arrowprops={"arrowstyle": "->", "color": red})
# The chi-square(1) density diverges at zero; the arrow marks continuation
# beyond the plot's vertical range, rather than inventing a finite peak.
ax_f.annotate("", xy=(0.245, 0.645), xytext=(0.34, 0.58),
              arrowprops={"arrowstyle": "->", "color": blue, "lw": 1.5})

fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight")
plt.close(fig)
