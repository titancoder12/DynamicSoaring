"""Writing results: CSV time series, the summary table and plots."""

import csv

from .energy import mean_rate
from .simulation import COLUMNS


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for row in rows:
            writer.writerow([f"{x:.4f}" for x in row])


def summarize(name, rows, info):
    """One summary line per case."""
    col = {c: i for i, c in enumerate(COLUMNS)}
    t = [r[col["t"]] for r in rows]
    first, last = rows[0], rows[-1]
    # How far the two frames drift apart during the run (J/kg). Zero in still
    # air; large when circling in wind, even though nothing real changed.
    gap = [r[col["e_ground"]] - r[col["e_air"]] for r in rows]
    gap = [g - gap[0] for g in gap]
    return {
        "case": name,
        "duration_s": round(t[-1] - t[0], 2),
        "height_start_m": round(first[col["h"]], 1),
        "height_end_m": round(last[col["h"]], 1),
        "airspeed_end_mps": round(last[col["airspeed"]], 2),
        "rate_air_Wkg": round(mean_rate(t, [r[col["e_air"]] for r in rows]), 3),
        "rate_ground_Wkg": round(mean_rate(t, [r[col["e_ground"]] for r in rows]), 3),
        "frame_gap_swing_Jkg": round(max(gap) - min(gap), 1),
        "note": info["reason"],
    }


def write_summary(path, summaries):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        writer.writerows(summaries)


def write_summary_md(path, title, summaries):
    """Same table as summary.csv, as Markdown (GitHub shows it nicely)."""
    keys = list(summaries[0].keys())
    lines = [f"# {title}", "",
             "rate = (energy at end - energy at start) / duration, in W/kg (= J/kg per s).",
             "`air` = air-relative energy, `ground` = ground-relative energy.",
             "`frame_gap_swing_Jkg` = how far (ground - air) energy moved during the run.", "",
             "| " + " | ".join(keys) + " |",
             "|" + "---|" * len(keys)]
    for s in summaries:
        lines.append("| " + " | ".join(str(s[k]) for k in keys) + " |")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def print_summary(summaries):
    print()
    print(f"{'case':<28}{'time s':>7}{'h start':>9}{'h end':>8}"
          f"{'air W/kg':>10}{'ground W/kg':>13}{'gap swing':>11}  note")
    print("-" * 100)
    for s in summaries:
        print(f"{s['case']:<28}{s['duration_s']:>7}{s['height_start_m']:>9}{s['height_end_m']:>8}"
              f"{s['rate_air_Wkg']:>10}{s['rate_ground_Wkg']:>13}{s['frame_gap_swing_Jkg']:>11}  {s['note']}")
    print("\nrate = (energy at end - energy at start) / duration, per kg of glider.")
    print("Negative = the glider lost energy. 'air' and 'ground' are the two energy frames.")
    print("gap swing = how far ground-relative minus air-relative energy moved during the run (J/kg).")


def plot_cases(path, results):
    """Energy vs time for every case, both frames. Needs matplotlib."""
    try:
        import matplotlib
        matplotlib.use("Agg")           # draw to a file, no window needed
        import matplotlib.pyplot as plt
    except ImportError:
        print("(matplotlib not installed - skipping plot)")
        return
    col = {c: i for i, c in enumerate(COLUMNS)}
    fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    for name, rows in results.items():
        t = [r[col["t"]] for r in rows]
        e_a0, e_g0 = rows[0][col["e_air"]], rows[0][col["e_ground"]]
        axes[0].plot(t, [r[col["e_air"]] - e_a0 for r in rows], label=name)
        axes[1].plot(t, [r[col["e_ground"]] - e_g0 for r in rows], label=name)
    axes[0].set_title("Air-relative specific energy (change from start)")
    axes[1].set_title("Ground-relative specific energy (change from start)")
    for ax in axes:
        ax.set_ylabel("J/kg")
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8)
    axes[1].set_xlabel("time (s)")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
