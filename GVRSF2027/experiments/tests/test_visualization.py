"""Check interactive output using short runs in temporary directories."""

import csv
import datetime
import json
import re

import pytest

from soaring_sim import run
from soaring_sim.simulation import COLUMNS
from soaring_sim.visualization import reconstruct_horizontal_positions


@pytest.fixture
def experiment(tmp_path, monkeypatch):
    class FrozenDateTime(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2026, 11, 21, 14)

    exp_dir = tmp_path / "GVRSF2027" / "experiments" / "EXP-001-sanity-checks"
    exp_dir.mkdir(parents=True)
    config = json.loads((run.EXPERIMENTS_ROOT / exp_dir.name / "config.json").read_text())
    config["simulation"]["duration_s"] = 0.2
    config["cases"] = config["cases"][:2]
    (exp_dir / "config.json").write_text(json.dumps(config))
    monkeypatch.setattr(run, "EXPERIMENTS_ROOT", exp_dir.parent)
    monkeypatch.setattr(run.datetime, "datetime", FrozenDateTime)
    return exp_dir


def results_path(experiment, run_id="2026-11-21_140000"):
    return experiment / "outputs" / run_id


def read_traces(path):
    html = path.read_text(encoding="utf-8")
    assert "plotly.js v" in html
    assert not re.search(r"<script\s+[^>]*\bsrc=", html)
    call = re.search(r'Plotly\.newPlot\(\s*"[^"]+",\s*', html)
    assert call is not None
    traces, _ = json.JSONDecoder().raw_decode(html, call.end())
    return traces


def test_run_writes_standalone_html_and_existing_outputs(experiment, capsys, tmp_path):
    run.main([str(experiment)])
    results_dir = results_path(experiment)
    html_path = results_dir / "flight_visualization.html"
    assert {path.name for path in results_dir.iterdir()} == {
        "config_used.json", "summary.csv", "summary.md", "energy.png",
        "still_air.csv", "uniform_headwind.csv", "flight_visualization.html",
    }
    assert not (tmp_path / "plots").exists()
    assert str(html_path) in capsys.readouterr().out
    traces = read_traces(html_path)
    for name in ("still_air", "uniform_headwind"):
        case = [trace for trace in traces if trace["name"] == name]
        assert [trace["type"] for trace in case] == ["scatter3d", "scatter3d"] + ["scatter"] * 4
        assert case[0]["z"][0] == pytest.approx(200)
        assert case[1]["text"] == ["Start", "End"]
        with (results_dir / f"{name}.csv").open() as csv_file:
            samples = list(csv.DictReader(csv_file))
        for trace, column in zip(case[2:], ("e_air", "e_ground", "h", "airspeed")):
            assert trace["x"] == pytest.approx([float(sample["t"]) for sample in samples])
            assert trace["y"] == pytest.approx([float(sample[column]) for sample in samples], abs=5.1e-5)


def test_same_second_runs_keep_distinct_results_and_plots(experiment):
    run.main([str(experiment)])
    first = results_path(experiment)
    original = {path.name: path.read_bytes() for path in first.iterdir()}
    run.main([str(experiment), "--case", "still_air"])
    second = results_path(experiment, "2026-11-21_140000-01")
    assert {path.name: path.read_bytes() for path in first.iterdir()} == original
    assert {trace["name"] for trace in read_traces(second / "flight_visualization.html")} == {"still_air"}
    assert not (second / "uniform_headwind.csv").exists()


def test_no_plot_skips_both_formats(experiment):
    run.main([str(experiment), "--case", "still_air", "--no-plot"])
    assert {path.name for path in results_path(experiment).iterdir()} == {
        "config_used.json", "summary.csv", "summary.md", "still_air.csv",
    }


def test_existing_explicit_output_directory_is_not_overwritten(experiment):
    prior = results_path(experiment)
    prior.mkdir(parents=True)
    summary = prior / "summary.md"
    summary.write_text("earlier results")
    with pytest.raises(FileExistsError):
        run.run_experiment(experiment, out_dir=prior)
    assert summary.read_text() == "earlier results"
    assert list(prior.iterdir()) == [summary]


def test_horizontal_positions_use_elapsed_time_and_trapezoidal_integration():
    rows = []
    for time, east, north in [(5.0, 2.0, 4.0), (5.5, 6.0, 0.0), (7.0, 4.0, -2.0)]:
        sample = {"t": time, "vg_east": east, "vg_north": north}
        rows.append([sample.get(column, 0.0) for column in COLUMNS])

    assert reconstruct_horizontal_positions(rows) == ([0.0, 2.0, 9.5], [0.0, 1.0, -0.5])
