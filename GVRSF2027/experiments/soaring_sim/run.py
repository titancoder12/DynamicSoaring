"""Run every case of one experiment.

Usage (from the experiments/ folder):
    python -m soaring_sim.run EXP-001-sanity-checks
    python -m soaring_sim.run EXP-001-sanity-checks --case still_air
    python -m soaring_sim.run EXP-001-sanity-checks --no-plot

Results go to  <experiment>/outputs/<date-time>/ :
    config_used.json   exact copy of the config for this run (reproducibility)
    <case>.csv         time series for each case
    summary.csv        one line per case
    summary.md         the same table in Markdown
    energy.png         plot of both energies (if matplotlib is installed)
"""

import argparse
import datetime
import json
import shutil
import sys
from pathlib import Path

from . import simulation  # noqa: F401  (sets JSBSIM_DEBUG before jsbsim loads)
import jsbsim

from .simulation import run_case
from .output import (write_csv, summarize, write_summary, write_summary_md,
                     print_summary, plot_cases)

EXPERIMENTS_ROOT = Path(__file__).resolve().parent.parent


def run_experiment(exp_dir, only_case=None, plot=True, out_dir=None, quiet=False):
    """Run an experiment folder. Returns (summaries, results, out_dir)."""
    exp_dir = Path(exp_dir)
    if not exp_dir.is_absolute() and not exp_dir.exists():
        exp_dir = EXPERIMENTS_ROOT / exp_dir
    config_path = exp_dir / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"No config.json in {exp_dir}")
    config = json.loads(config_path.read_text())

    sim_cfg = config["simulation"]
    aircraft_dir = None
    if sim_cfg.get("aircraft_dir"):                 # custom gliders (see aircraft/README.md)
        aircraft_dir = (EXPERIMENTS_ROOT / sim_cfg["aircraft_dir"]).resolve()

    cases = config["cases"]
    if only_case:
        cases = [c for c in cases if c["name"] == only_case]
        if not cases:
            raise ValueError(f"No case named '{only_case}' in {config_path}")

    if out_dir is None:
        stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        out_dir = exp_dir / "outputs" / stamp
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(config_path, out_dir / "config_used.json")

    if not quiet:
        print(f"Experiment: {config.get('name', exp_dir.name)}")
        print(f"JSBSim {jsbsim.__version__}, aircraft '{sim_cfg['aircraft']}', "
              f"{sim_cfg.get('rate_hz', 120)} Hz, {sim_cfg['duration_s']} s per case")

    summaries, results = [], {}
    for case in cases:
        rows, info = run_case(sim_cfg, case, aircraft_dir)
        write_csv(out_dir / f"{case['name']}.csv", rows)
        summaries.append(summarize(case["name"], rows, info))
        results[case["name"]] = rows

    write_summary(out_dir / "summary.csv", summaries)
    write_summary_md(out_dir / "summary.md", config.get("name", exp_dir.name), summaries)
    if plot:
        plot_cases(out_dir / "energy.png", results)
    if not quiet:
        print_summary(summaries)
        print(f"\nSaved to {out_dir}")
    return summaries, results, out_dir


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run one soaring experiment folder.")
    parser.add_argument("experiment", help="experiment folder, e.g. EXP-001-sanity-checks")
    parser.add_argument("--case", help="run only the case with this name")
    parser.add_argument("--no-plot", action="store_true", help="skip the plot")
    args = parser.parse_args(argv)
    run_experiment(args.experiment, args.case, plot=not args.no_plot)


if __name__ == "__main__":
    sys.exit(main())
