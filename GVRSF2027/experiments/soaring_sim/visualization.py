"""Build an offline flight visualization from the same samples as the CSVs."""

from itertools import pairwise

from plotly import graph_objects as go
from plotly.colors import qualitative
from plotly.subplots import make_subplots

from .simulation import COLUMNS


COL = {name: index for index, name in enumerate(COLUMNS)}
METRICS = (
    ("e_air", "Air-relative specific energy", "J/kg", 2, 1),
    ("e_ground", "Ground-relative specific energy", "J/kg", 2, 2),
    ("h", "Altitude above ground", "m", 3, 1),
    ("airspeed", "Airspeed", "m/s", 3, 2),
)


def reconstruct_horizontal_positions(rows):
    """Integrate logged ground velocity using the trapezoidal rule in metres."""
    east, north = [0.0], [0.0]
    time, east_velocity, north_velocity = (COL[key] for key in ("t", "vg_east", "vg_north"))
    for previous, current in pairwise(rows):
        dt = current[time] - previous[time]
        east.append(east[-1] + dt * (previous[east_velocity] + current[east_velocity]) / 2)
        north.append(north[-1] + dt * (previous[north_velocity] + current[north_velocity]) / 2)
    return east, north


def write_flight_visualization(out_dir, results, experiment_name):
    """Export the standalone flight visualization and return its path."""
    fig = make_subplots(
        rows=3, cols=2,
        specs=[[{"type": "scene", "colspan": 2}, None], [{}, {}], [{}, {}]],
        row_heights=[0.56, 0.22, 0.22],
        vertical_spacing=0.10,
        subplot_titles=("Flight trajectory · ○ Start · ◆ End", *(m[1] for m in METRICS)),
    )
    palette = qualitative.Dark24
    for index, (name, rows) in enumerate(results.items()):
        color = palette[index % len(palette)]
        east, north = reconstruct_horizontal_positions(rows)
        altitude = [row[COL["h"]] for row in rows]
        time = [row[COL["t"]] for row in rows]
        hover_data = [
            [row[COL[key]] for key in ("t", "airspeed", "e_air", "e_ground")]
            for row in rows
        ]
        hover = (
            "Time: %{customdata[0]:.2f} s<br>Altitude: %{z:.2f} m"
            "<br>Airspeed: %{customdata[1]:.2f} m/s"
            "<br>Air-relative energy: %{customdata[2]:.2f} J/kg"
            "<br>Ground-relative energy: %{customdata[3]:.2f} J/kg<extra>%{fullData.name}</extra>"
        )
        fig.add_trace(go.Scatter3d(
            x=east, y=north, z=altitude, name=name, legendgroup=name,
            mode="lines", line={"color": color, "width": 5},
            customdata=hover_data, hovertemplate=hover,
        ), row=1, col=1)
        fig.add_trace(go.Scatter3d(
            x=[east[0], east[-1]], y=[north[0], north[-1]], z=[altitude[0], altitude[-1]],
            name=name, legendgroup=name, showlegend=False, mode="markers",
            marker={"color": color, "size": 6, "symbol": ["circle-open", "diamond"]},
            text=["Start", "End"], customdata=[hover_data[0], hover_data[-1]],
            hovertemplate="%{text}<br>" + hover,
        ), row=1, col=1)

        for key, label, unit, row_index, col_index in METRICS:
            fig.add_trace(go.Scatter(
                x=time, y=[row[COL[key]] for row in rows], name=name,
                mode="lines", line={"color": color}, legendgroup=name, showlegend=False,
                hovertemplate=f"Time: %{{x:.2f}} s<br>{label}: %{{y:.2f}} {unit}<extra>%{{fullData.name}}</extra>",
            ), row=row_index, col=col_index)

    for _, _, unit, row_index, col_index in METRICS:
        fig.update_xaxes(title_text="Time (s)", row=row_index, col=col_index)
        fig.update_yaxes(title_text=unit, row=row_index, col=col_index)
    fig.update_xaxes(matches="x", selector=lambda axis: axis.anchor != "y")
    fig.update_layout(
        title=experiment_name, height=1250, template="plotly_white",
        margin={"t": 130, "b": 65},
        legend={"orientation": "h", "y": 1.04, "yanchor": "bottom", "groupclick": "togglegroup"},
        scene={
            "xaxis_title": "East (m)", "yaxis_title": "North (m)",
            "zaxis_title": "Altitude (m)", "aspectmode": "cube",
            "camera": {"eye": {"x": 1.45, "y": 1.45, "z": 1.05}},
        },
    )
    path = out_dir / "flight_visualization.html"
    temporary_path = path.with_suffix(".html.tmp")
    try:
        fig.write_html(temporary_path, include_plotlyjs=True, config={"scrollZoom": True})
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)
    return path
