# Bio-Inspired Cooperative Fixed-Wing Flight

**Status:** Idea / candidate CWSF 2027 investigation (2026-10-18)

## Research question
Can decentralized local interaction rules maintain safe formation flight despite communication limits?

## Concept
Multiple fixed-wing aircraft in physics simulation; optional hardware-in-loop.

## Hypothesis (to test)
The proposed approach may improve a defined primary metric relative to appropriate baselines under specified conditions; this is an untested prediction, not a result.

## Independent variables
Team size, communication radius, latency, packet loss, formation geometry.

## Dependent variables
Formation error, separation violations, message count, resilience and control effort.

## Baselines and experimental design
Leader-follower, consensus formation control, flocking rules.

## Ablations and robustness
Ablate neighbor sensing, topology and communication.

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
