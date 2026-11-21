# aircraft/ — your own glider models

Empty for now. This is where your own JSBSim glider files go, for example an
albatross-scale glider.

## Folder layout JSBSim expects

JSBSim finds a model by name as `<aircraft folder>/<Name>/<Name>.xml`:

```
aircraft/
  Albatross/
    Albatross.xml
```

## Starting point

Copy a built-in sailplane and edit its numbers. To find where JSBSim keeps
its built-in models:

```bash
python -c "import jsbsim, os; print(os.path.join(jsbsim.get_default_root_dir(), 'aircraft'))"
```

Copy for example `SGS/SGS.xml` (full-size sailplane, about 15 m span) or
`minisgs/`, then rename the file and folder to match (e.g. `Albatross/Albatross.xml`).
The values you will most likely change are in `<metrics>` (wing area, span,
chord), `<mass_balance>` (mass and inertia) and `<aerodynamics>` (lift and
drag). Write down in your Digital Logbook where each number comes from.

## Using it in an experiment

In that experiment's `config.json`:

```json
"aircraft": "Albatross",
"aircraft_dir": "aircraft",
```

`aircraft_dir` is relative to the `experiments/` folder. When it is set,
JSBSim looks ONLY in this folder, so built-in models like `SGS` can't be
loaded in that experiment unless you copy them in too.

## Check it before you trust it

Before using a new model in a real comparison, run it in still air (copy
`EXP-001-sanity-checks`, change the aircraft) and check that it glides
steadily, that the sink rate and glide ratio are believable for its size,
and that the tests in `tests/` still pass the same way.
