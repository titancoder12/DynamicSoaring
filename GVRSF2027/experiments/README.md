# GVRSF 2027 — JSBSim experiments

Starter code for flying a simulated glider in [JSBSim](https://github.com/JSBSim-Team/jsbsim)
and measuring its energy in different winds. It is a **starting point**. It has
no AI/RL controller and no dynamic-soaring controller, and the numbers it
produces are **sanity checks, not project results**. Building the controllers
and running the real comparison is your work.

## Folder layout

```
experiments/
  README.md            this file
  requirements.txt     Python packages (pinned versions that were tested)
  soaring_sim/         shared code that every experiment uses
    run.py             the runner:  python -m soaring_sim.run <experiment>
    simulation.py      runs one wind case in JSBSim, step by step
    wind.py            wind models (still, uniform, linear shear, log shear)
    energy.py          ground-relative and air-relative specific energy
    controllers.py     the default glide controller + a template for yours
    output.py          CSV, summary tables, plots
    visualization.py  offline Plotly flight paths and time series
    units.py           feet <-> metres, g
  aircraft/            your own glider models later (see aircraft/README.md)
  _template/           copy this to start a new experiment
  EXP-001-sanity-checks/   the first experiment
    config.json        what to run
    README.md          question, hypothesis, setup, results, conclusion
    outputs/           one date-time folder per run (committed to Git)
  tests/               automatic sanity checks (pytest)
```

## 1. Install (once)

You need **Python 3.10 or newer**. Check with `python3 --version`
(Windows: `py --version`). If you don't have it, install it from
[python.org](https://www.python.org/downloads/).

Open a terminal in this `experiments/` folder, then:

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell)**
```powershell
py -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
If PowerShell blocks the activate script, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, or use Command
Prompt with `venv\Scripts\activate.bat`.

Check JSBSim works:
```bash
python -c "import jsbsim; print(jsbsim.__version__)"
```
It should print `1.3.3`. Each new terminal needs the `activate` line again
before running anything. The `venv/` folder is not committed to Git.

## 2. Run the first experiment

```bash
python -m soaring_sim.run EXP-001-sanity-checks              # all cases
python -m soaring_sim.run EXP-001-sanity-checks --case still_air   # one case
python -m soaring_sim.run EXP-001-sanity-checks --no-plot
python -m pytest tests                                       # sanity checks
```

All 7 cases take a few seconds. The runner prints a summary table and saves
everything in `EXP-001-sanity-checks/outputs/<date>_<time>/`:

| file | what it is |
|---|---|
| `config_used.json` | exact copy of the config used (so the run can be repeated) |
| `<case>.csv` | time series, one row every 0.1 s |
| `summary.csv`, `summary.md` | one line per case |
| `energy.png` | both energies vs time, all cases |
| `flight_visualization.html` | interactive 3D flight paths and time series |

### Open the interactive visualization

The runner automatically saves the HTML alongside the CSVs, summaries, and
`energy.png`, and prints its full path. Runs started in the same second get
distinct IDs. Open the HTML file in a browser. It includes Plotly and the data
needed to work offline.

On macOS, from `GVRSF2027/experiments/`, replace `<run-id>` with the folder
name printed by the runner and open the file:

```bash
open "EXP-001-sanity-checks/outputs/<run-id>/flight_visualization.html"
```

- **3D trajectory (m).** East and North show displacement from each case's
  starting point, reconstructed by integrating the logged ground velocities
  over the sample timestamps. Altitude comes from `h`, the logged height above
  ground. The path is reconstructed after the run from the logged samples.
  The display scales each axis independently to keep shallow glides visible.
  Use the 3D camera controls to rotate, zoom, or pan. Hover for time, altitude,
  airspeed, and both specific energies. The open circle marks the start and
  the diamond marks the end.
- **Air-relative and ground-relative specific energy (J/kg).** The separate
  time series show the logged energy per unit mass in each reference frame.
  Treat transient changes and differences between frames as diagnostic
  observations. Evidence of sustained dynamic soaring requires evaluating
  energy over a complete cycle.
- **Altitude (m) and airspeed (m/s).** These time series show the logged height
  above ground and the glider's speed relative to the surrounding air.

Click a case in the legend to show or hide it across all five graphs. Use
`--case <name>` to include a single case or `--no-plot` to save the CSVs and
summaries without generating either `energy.png` or the interactive HTML.

**Outputs are committed to Git on purpose.** Every run stays on record with
its config, so you (and the judges) can trace any number back to the run that
produced it. Don't delete or edit old runs. If a run was a mistake, say so in
your logbook.

### CSV columns (SI units)
`t` time (s) · `h` height above the surface (m) · `airspeed` (m/s) ·
`vg_north, vg_east, vg_down` ground velocity (m/s) · `ground_speed` horizontal (m/s) ·
`w_north, w_east` wind = velocity of the air (m/s) · `theta_deg, phi_deg, psi_deg`
pitch, bank, heading · `elevator, aileron` commands (-1..1) ·
`e_ground, e_air` specific energy in each frame (J/kg).

### Reading the summary
- `rate_air_Wkg`, `rate_ground_Wkg`: (energy at end − energy at start) ÷
  duration, in W/kg, for each frame. Negative = energy lost.
- `frame_gap_swing_Jkg`: how far the two frames moved apart during the run.

### What you should see (sanity outcomes)
- Still air: energy falls at roughly −9.5 W/kg (about 1 m/s of sink); both frames match.
- Uniform wind, straight or circling: **air-relative** rate equals still air.
- Uniform wind, circling: **ground-relative** energy rises and falls by
  hundreds of J/kg around the circle. That's an effect of the frame, not real
  energy.
- Shear: air-relative rate is worse than still air flying into the wind and
  better flying with it (this profile has the wind stronger higher up and the
  glider descending).

`python -m pytest tests` checks the first two automatically. If a test fails
after you change code, fix that first.

## 3. Configure (`config.json`)

```jsonc
"simulation": {
  "aircraft": "SGS",          // JSBSim model name (built-in, or your own in aircraft/)
  "aircraft_dir": null,       // null = built-in models; "aircraft" = use experiments/aircraft/
  "rate_hz": 120,             // physics steps per second (dt = 1/120 s). Keep fixed within a comparison.
  "duration_s": 60,           // length of each case
  "log_every_steps": 12,      // write a CSV row every 12 steps = 0.1 s (keeps files small)
  "min_height_m": 5,          // stop early if the glider gets this low
  "start": {"height_m": 200, "airspeed_mps": 27, "heading_deg": 0, "flight_path_deg": -2},
  "controller": {"type": "glide", "target_airspeed": 27, "bank_deg": 0}
},
"cases": [
  {"name": "still_air", "wind": {"type": "still"}},
  {"name": "uniform_headwind", "wind": {"type": "uniform", "speed": 8, "from_deg": 0}},
  {"name": "shear", "wind": {"type": "linear_shear", "speed_ref": 8, "height_ref_m": 200,
                              "gradient_per_s": 0.05, "from_deg": 0},
   "controller": {"bank_deg": 20}}       // a case can override controller or start settings
]
```

- Heading: 0 = north, 90 = east. `from_deg` is the direction the wind
  comes **from**, like a weather report.
- Wind types: `still`, `uniform`, `linear_shear`, `log_shear` (see `soaring_sim/wind.py`).
- Controller types: `glide`, `hands_off`, and `mine` (your template, see below).
- The real albatross wind gradient is in the lowest ~20 m over the sea. EXP-001
  starts at 200 m only to keep the sanity checks far from the surface.

## 4. Create a new experiment (step by step)

Every experiment is its own folder in `experiments/`. The shared code in
`soaring_sim/` stays the same; an experiment is just a `config.json` (what to
run) plus a `README.md` (why, and what you found) plus its `outputs/`.

### Step 1: Copy the template
Copy the whole `_template/` folder and rename the copy with the **next number**
and a short name in lowercase words joined by dashes:

```bash
cp -r _template EXP-002-headwind-sweep          # macOS / Linux
```
```powershell
Copy-Item -Recurse _template EXP-002-headwind-sweep   # Windows PowerShell
```

Never reuse or renumber an old experiment. If you want to redo one with a
change, make a new number (e.g. `EXP-003-headwind-sweep-v2`) and say in its
README which experiment it follows from.

### Step 2: Write the plan *before* running
Open the new folder's `README.md` and fill in:
- **Question**: one sentence, e.g. "How does steady headwind strength change
  the air-relative energy rate of the SGS in straight glide?"
- **Hypothesis**: what you expect and why, with a number if you can.
- **Setup**: aircraft, controller, wind cases, duration, and **the one thing
  you are changing** compared with the earlier experiment.

Writing this first is what makes it an experiment rather than a fishing trip.
Judges look for it.

### Step 3: Edit `config.json`
Change `"name"`, then the settings (all fields are explained in section 3):
- `simulation`: aircraft, start height/speed/heading, duration, controller.
  These apply to every case unless a case overrides them.
- `cases`: a list. Each case needs a unique `"name"` (it becomes the CSV file
  name) and a `"wind"`. A case may also have its own `"controller"` or
  `"start"` settings, which override the shared ones for that case only.

Example: a headwind sweep that changes **only** the wind speed:

```json
"cases": [
  {"name": "still_air",   "wind": {"type": "still"}},
  {"name": "headwind_4",  "wind": {"type": "uniform", "speed": 4,  "from_deg": 0}},
  {"name": "headwind_8",  "wind": {"type": "uniform", "speed": 8,  "from_deg": 0}},
  {"name": "headwind_12", "wind": {"type": "uniform", "speed": 12, "from_deg": 0}}
]
```

Always include a **still-air** case as your control, so every result can be
compared with a no-wind reference.

### Step 4 (optional): Use your own controller or glider
- **Controller:** write it in `soaring_sim/controllers.py` by filling in the
  `MyController` template, then set `"controller": {"type": "mine"}` in the
  config. Before trusting it in shear, check it gains no energy in still air
  or uniform wind (`python -m pytest tests`, plus a still-air case).
- **Glider:** put your model in `aircraft/` (see `aircraft/README.md`) and set
  `"aircraft": "<your model name>", "aircraft_dir": "aircraft"`.

If you change shared code in `soaring_sim/`, rerun `python -m pytest tests`
and say in your logbook what you changed, because it affects every later
experiment.

### Step 5: Run it
From the `experiments/` folder, with the venv activated:

```bash
python -m soaring_sim.run EXP-002-headwind-sweep
python -m soaring_sim.run EXP-002-headwind-sweep --case headwind_8   # just one case
```

Results appear in `EXP-002-headwind-sweep/outputs/<date>_<time>/`. Each run
makes a new folder, so running again never overwrites earlier results.

Or ask Albert to run it: push the folder to GitHub (step 7) and tell Dad the
experiment name; Albert runs it exactly as configured, commits the outputs to
that folder and sends back a summary and review.

### Step 6: Write up results
Back in the experiment's `README.md`:
- **Results**: name the run folder you are reporting, paste or summarize
  `summary.md`, and describe `energy.png`. Report numbers with units.
- **Conclusion**: was the hypothesis supported? What surprised you? What could
  be wrong (model, controller, settings)? What should the next experiment change?

Add a dated entry in your **Digital Logbook**: experiment name, run folder,
what you changed, what you saw, and what you'll do next.

### Step 7: Commit and push
Commit the whole experiment folder **including `outputs/`**:

```bash
git add EXP-002-headwind-sweep
git commit -m "EXP-002 headwind sweep: config, plan and first run"
git push
```

### Checklist
- [ ] New numbered folder copied from `_template/`
- [ ] Question, hypothesis and setup written before running
- [ ] Only one thing changed compared with the previous experiment
- [ ] Still-air control case included
- [ ] Tests pass if shared code changed
- [ ] Results and conclusion written, logbook entry made
- [ ] Folder, including `outputs/`, committed and pushed

## 5. Your next steps

These are your decisions and your work:

1. **Choose your energy frame.** Run EXP-001, study the circling and shear
   cases, and reread Sachs (2005, ground-relative) and Richardson (2015,
   air-relative). Decide which frame your main measurement uses, write down
   why in your logbook, and fix it *before* testing controllers.
2. **Make an albatross-scale glider** in `aircraft/` (see `aircraft/README.md`)
   and check it in still air first.
3. **Write your controllers** in `soaring_sim/controllers.py`, starting from
   the `MyController` template: the fixed-trajectory one, then the
   conventional one, then the AI one. Every controller must pass the
   still-air and uniform-wind checks (no free energy) before you test it in shear.
4. **Wind for the real tests:** low-altitude `log_shear` profiles, and a set of
   **held-out** test winds that you never use while designing or training.
   Pick them and write them down in advance.
5. **Log every run** in your Digital Logbook with the date and the output
   folder name.

## Limitations of this starter
- `SGS` is a full-size human-carrying sailplane, not an albatross.
- No turbulence, gusts, or vertical wind; wind depends only on height.
- The glide controller is deliberately simple and doesn't hold its target
  speed exactly. It isn't a baseline for your project.
- Energy rate is measured from start to end of each case. For your real
  measurement you'll need to decide how to measure per soaring cycle.
