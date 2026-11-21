# Adaptive Fixed-Wing Flight Control

**Status:** Idea / candidate CWSF 2027 investigation (2026-10-18)

## Research question
Can an adaptive controller outperform PID and model-predictive control under unseen wind disturbances?

## Concept
Single fixed-wing UAV; simulated and eventually FW-01 validation.

## Hypothesis (to test)
The proposed approach may improve a defined primary metric relative to appropriate baselines under specified conditions; this is an untested prediction, not a result.

## Independent variables
Wind gust magnitude, frequency, turbulence spectrum, sensor noise and model mismatch.

## Dependent variables
Trajectory error, attitude recovery, control effort, energy proxy, failure rate.

## Baselines and experimental design
PID, tuned LQR/MPC, learned controller; matched tuning budgets and identical wind seeds.

## Ablations and robustness
Ablate wind estimates, training domain randomization and observation history.

## Experimental integrity
Pre-register hypotheses and metrics before final experiments. Use repeated independent seeds/trials, uncertainty intervals and paired comparisons; report negative results and failure modes. Separate simulation, hardware-in-loop and physical evidence. Treat energy proxies as estimates unless calibrated against measured electrical power.

## CWSF 2027 feasibility and safety
Status: brainstormed research proposal, not an implemented or validated result. Begin with simulation and bench tests. Physical flights require risk assessment, applicable Transport Canada compliance, safe airspace and adult supervision; multi-aircraft flight is optional. Prioritize one falsifiable scientific contribution over a polished demonstration.

## Related work to review
Search peer-reviewed literature before claiming novelty. Record authors, DOI, assumptions, baseline methods and gaps. For the combined idea, investigate existing distributed reinforcement-learning formation control under external disturbances; wind-information sharing alone must be shown to contribute something not already established.

## Next steps
1. Conduct focused literature review and novelty matrix.
2. Specify governing dynamics, measurement protocol and baseline implementations.
3. Run a small feasibility experiment before selecting this as the final project.
