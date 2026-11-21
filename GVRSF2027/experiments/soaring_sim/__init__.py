"""soaring_sim: a small shared toolkit for Christopher's JSBSim glider experiments.

Every experiment folder (EXP-001-..., EXP-002-..., ...) uses this package
instead of copying code, so a bug fixed here is fixed for every experiment.

Modules:
    units        unit conversions (JSBSim works in feet; we work in SI)
    wind         wind models: still air, uniform wind, wind shear
    energy       specific-energy formulas (ground-relative and air-relative)
    controllers  the default "glide" controller + a template for your own
    simulation   runs ONE wind case in JSBSim and returns a time series
    output       writes CSV files, the summary table and plots
    run          command-line entry point:  python -m soaring_sim.run <experiment-folder>
"""
