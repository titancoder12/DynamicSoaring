# Measurement selection for physical-model discrimination

**Working question:** Which measurement should be taken to distinguish competing physical explanations?  
**Status:** Candidate architecture F; strong science reserve.

## Scientific problem

Two different physical processes can fit the same sparse observations. A sensing system that minimizes prediction error may still fail to identify which process is actually responsible.

## Proposed research question

> Does selecting measurements where competing physical models disagree identify the correct process more efficiently than selecting measurements only to minimize average map uncertainty?

## Proposed hypothesis

Disagreement-targeted measurements should reduce model confusion in informative regions, provided the candidate model set includes a useful approximation of reality. The benefit may disappear when every candidate model is wrong.

## Proposed experiment

Possible physical analogue:

- heat diffusion/advection;
- controllable airflow/temperature;
- independently measured reference state.

Compare:

- random/uniform measurements;
- variance-reduction sampling;
- model-disagreement sampling;
- full-reference fit.

Evaluate:

- model-selection error;
- parameter error;
- predictive error;
- sample/resource cost.

Include a deliberate misspecified-model condition where the true process lies outside the candidate set.

## Practical solution path

An airborne system could use this principle to decide where to sample when the goal is not simply making a map, but determining **why** an observed field has its shape.

Potential applications include:

- atmospheric transport;
- wildfire plume behaviour;
- pollutant dispersion;
- thermal anomalies.

## Novelty risk

Active model discrimination and adaptive experimental design are established research areas. The project must identify a narrow physical setting and demonstrate a meaningful difference between “predict accurately” and “identify the right process.”

## CWSF-analysis connection

This directly matches the **scientific inference system** archetype: observations → validated inference → physical relationship/explanation.

It is scientifically strong but experimentally more demanding than simple mapping.

## References

1. **CWSF 2026 Gold project:** *Ghosts in the Stream: Probing Dark Matter in the GD-1 Stellar Stream with Simulation-Based Inference.*  
   https://partner.projectboard.world/ysc/project/ghosts-in-the-stream-probing-dark-matter-in-the-gd-1-stellar-stream-with-simulation-based-inference

2. **CWSF 2025 Gold project:** *Probing Galaxy Disk Sizes Using the Largest Ever Catalog of Ca II Absorbers.*  
   https://partner.projectboard.world/ysc/project/probing-galaxy-disk-sizes-using-the-largest-ever-catalog-of-ca-ii-absorbers

3. **CWSF 2026 Silver project:** *Modelling the Light Echo in Active Galaxy BL Lacertae Using High-Cadence Light-Curve Data.*  
   https://partner.projectboard.world/ysc/project/modelling-the-light-echo-in-active-galaxy-bl-lacertae-using-high-cadence-light-curve-data

4. **Krause, Singh & Guestrin (2008).** Information-driven sensor placement.  
   https://www.jmlr.org/papers/v9/krause08a.html
