"""
Radar chart of baseline scores across the 13 sections.

Usage:
    python radar_chart.py

Regenerate quarterly after each re-baseline; save output as
    progress/radar_YYYY-MM-DD.png

Sections and scores are hard-coded from `progress/baseline_scores.md`.
Update the SCORES dict when you retake.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

SCORES: dict[str, float] = {
    "I Prob & Comb": 1.20,
    "II Puzzles": 1.50,
    "III Markov": 1.50,
    "IV Cont-time": 0.60,
    "V Stoch Ctrl": 0.50,
    "VI Deriv": 1.20,
    "VII Lin Alg": 1.33,
    "VIII Calc/DE": 1.00,
    "IX Stats": 1.00,
    "X Algo/DS": 1.20,
    "XI Info Th": 0.50,
    "XII Game Th": 0.00,
    "XIII Measure": 0.00,
}

DATE_LABEL = "2026-07-24 (baseline)"


def plot_radar(scores: dict[str, float], date_label: str, out_path: Path) -> None:
    labels = list(scores.keys())
    values = list(scores.values())
    n = len(labels)

    # close the loop
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    values_closed = values + values[:1]
    angles_closed = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={"projection": "polar"})
    ax.plot(angles_closed, values_closed, linewidth=2, color="#1f77b4")
    ax.fill(angles_closed, values_closed, alpha=0.25, color="#1f77b4")

    # reference rings at rubric levels
    for level, txt in [(1, "Cold"), (2.5, "Rusty"), (3.5, "Working"), (5, "Solid")]:
        ax.plot(angles_closed, [level] * (n + 1), linestyle="--",
                linewidth=0.6, color="grey", alpha=0.5)
        ax.text(np.pi / 2, level + 0.05, txt, fontsize=7, color="grey", ha="center")

    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8)
    ax.set_title(f"Baseline radar — {date_label}\nMean = {np.mean(values):.2f}",
                 fontsize=12, pad=20)

    plt.tight_layout()
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    here = Path(__file__).parent
    out = here / "radar_2026-07-24_baseline.png"
    plot_radar(SCORES, DATE_LABEL, out)
