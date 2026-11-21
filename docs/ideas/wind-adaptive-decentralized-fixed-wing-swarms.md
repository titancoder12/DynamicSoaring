# Wind-Adaptive Decentralized Fixed-Wing Swarms (Ideas 1 + 3)

**Status:** Idea / candidate CWSF 2027 investigation (2026-10-18)

## Research question
Does sharing compact local wind estimates improve formation robustness and efficiency beyond independent adaptive control and conventional distributed control?

## Concept
Physics-based multi-fixed-wing simulation, hardware-in-loop, optional single FW-01 field validation.

## Hypothesis (to test)
The proposed approach may improve a defined primary metric relative to appropriate baselines under specified conditions; this is an untested prediction, not a result.

## Independent variables
Wind heterogeneity, unseen gusts, packet loss, latency, team size, neighbor radius.

## Dependent variables
Formation RMS error, collision/separation violations, recovery time, communication bytes, energy proxy.

## Baselines and experimental design
2x2 factorial: independent PID; distributed conventional control; independent RL; decentralized MARL. Also compare cooperative policies with/without wind-estimate sharing.

## Ablations and robustness
Ablate shared wind information, communication bandwidth, recurrent memory and agent count; test unseen wind fields and model mismatch.

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
