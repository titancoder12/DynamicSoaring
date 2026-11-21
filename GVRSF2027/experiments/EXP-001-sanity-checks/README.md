# EXP-001 — Sanity checks: still air, uniform wind, wind shear

A starter experiment. It checks that the simulator and the energy bookkeeping
behave the way physics says they must **before** any controller comparison.
These are sanity checks, not project results.

## Question
Does the simulation do the physically expected thing with a plain glide
controller (no soaring tricks) in still air, uniform wind, and wind shear?
How different are the ground-relative and air-relative energy frames?

## Hypothesis (what physics predicts)
1. **Still air:** the glider loses energy steadily (drag). Both frames give
   the same number.
2. **Uniform, steady wind:** the air-relative energy rate is the **same** as
   in still air. A steady wind can't give free energy; it only carries the
   glider along.
3. **Uniform wind, circling:** air-relative energy is still the same as in
   still air, but ground-relative energy swings up and down as the glider
   turns downwind and upwind. That swing is **not** real energy gain.
4. **Wind shear:** descending through a shear changes the airspeed, so the
   air-relative rate differs from still air. With this profile (wind stronger
   higher up) a glider flying **into** the wind and descending loses airspeed
   (worse than still air). One flying **with** the wind gains airspeed
   (better than still air, but still negative overall).

## Setup (`config.json`)
- Aircraft: JSBSim built-in `SGS` sailplane (full-size, ~14 m span, **not** albatross-sized).
- Start: 200 m, 27 m/s airspeed, heading north, -2° flight path.
- Controller: `glide` (holds about 27 m/s and a fixed bank angle). No soaring logic.
- 60 s per case, physics at 120 Hz, logged every 0.1 s.
- Wind cases:

| case | wind | bank |
|---|---|---|
| `still_air` | none | 0° |
| `uniform_headwind` | 8 m/s from north (glider heads north) | 0° |
| `uniform_tailwind` | 8 m/s from south | 0° |
| `still_air_circling` | none | 20° |
| `uniform_wind_circling` | 8 m/s from north | 20° (≈ one full circle in 60 s) |
| `shear_headwind` | 8 m/s at 200 m, +0.05 (m/s)/m higher, from north | 0° |
| `shear_tailwind` | same, from south | 0° |

## How to run
From the `experiments/` folder:
```bash
python -m soaring_sim.run EXP-001-sanity-checks
python -m pytest tests            # automatic pass/fail checks for hypotheses 1-2
```

## What changed from the previous experiment
First experiment.

## Results
The starter's reference run is committed in `outputs/` (the earliest
date-time folder). **Rerun it yourself** and check you get the same numbers
(the simulation is deterministic, so they should match exactly on the same
JSBSim version). Then write down here and in your Digital Logbook:

- Which hypotheses were confirmed?
- How big was the ground-relative "gain" in `uniform_wind_circling` at its
  peak (see `energy.png`), even though the air-relative energy fell steadily?
- In the shear cases, how big was the difference from still air? Can you
  explain the size with a back-of-envelope estimate? (Hint: the airspeed
  change per second ≈ shear gradient × sink rate.)

## Conclusion
Your words: is the simulator ready for controller experiments? Which energy
frame will you use for your main measurement, and why?

## Things found while building this (JSBSim notes)
- **Wind sign:** `atmosphere/wind-north-fps > 0` means the air moves north.
  Checked: heading north at 27 m/s over the ground with +8 m/s gives 19 m/s
  airspeed. Configs use the weather-report "from" direction instead, and
  `soaring_sim/wind.py` converts it.
- **Initial wind settings (`ic/vw-*`) were not used.** In tests they gave a
  starting airspeed that didn't match the requested one (e.g. 11 m/s instead
  of 27 m/s with 8 m/s wind). The code sets the starting ground velocity as
  airspeed + wind instead, so every case starts at exactly 27 m/s airspeed.
- **`run_ic()` resets the wind to zero**, so the wind is set after it, and
  again every time step from the glider's current height (needed for shear).
- **No trim for gliders:** JSBSim's trim routine fails ("udot doesn't appear
  to be trimmable") because there is no engine. The glide controller settles
  the glider within ~15 s instead. Hands-off (`hands_off` controller), the
  SGS oscillates up and down (phugoid) by several degrees of pitch.
- **Speed hold isn't exact:** the simple controller settles at about 27.9 m/s
  straight (29.5 m/s at 20° bank), not exactly 27, because it has no
  integral term. The early speed-up is part of every case, so the
  comparisons are still fair.
- JSBSim models a round, rotating Earth, so a uniform wind is not *perfectly*
  identical to still air. In this run the difference was below 0.001 W/kg.
