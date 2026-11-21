# Recalibration versus exploration

**Working question:** When should a sensing team stop exploring to recalibrate?  
**Status:** Strong physical-measurement architecture; originally shortlisted as candidate C.

## Scientific problem

Distributed low-cost sensors drift, develop offsets, or disagree. A team can mistake sensor error for real spatial structure. Shared biased observations may then spread the error across the map.

The central tradeoff is:

> Spend limited time measuring new locations, or spend some of that time checking whether the sensors themselves are still trustworthy.

## Proposed research question

> At what combinations of sensor drift, reference uncertainty and revisit cost does reference checking improve a distributed field estimate compared with exploration-only sensing?

## Proposed hypothesis

Reference measurements should improve mapping when drift is large enough to create false structure, but waste resources when drift is negligible. An error-triggered policy may reduce unnecessary calibration while still controlling mapping error.

## Proposed experiment

- Several inexpensive light or temperature sensors.
- Independent stable reference.
- Controlled injected offsets first; physical drift tests later.
- Vary:
  - offset magnitude;
  - drift rate;
  - revisit cost;
  - reference uncertainty.
- Compare:
  - no recalibration;
  - fixed-interval calibration;
  - centralized estimation;
  - published uncertainty-driven scheduling;
  - proposed calibration/coverage policy.
- Evaluate:
  - map error;
  - estimated sensor offsets;
  - coverage;
  - resource use.

## Practical solution path

The practical system would become a distributed aerial or ground sensor team that knows when to stop collecting new observations and instead obtain a common reference measurement.

In an airborne system, this could mean aircraft periodically co-observe a reference region or compare against a trusted instrument.

## Novelty risk

Adaptive calibration and uncertainty-driven calibration scheduling are already active research areas. The contribution cannot simply be “calibrate when uncertain.”

The candidate needs a distinct experimentally characterized **calibration-versus-coverage tradeoff**, identifiability result, or practical resource-allocation rule.

## CWSF-analysis connection

This is closely aligned with the repo's **measurement instrument** archetype:

hard-to-measure quantity → instrument/model → independent reference → characterized error.

Relevant internal reports:

- [Project archetypes](../../reports/analysis/project-archetypes.md)
- [Candidate architectures](../../reports/analysis/cwsf2027-candidate-architectures.md)
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md)

## References

1. **Hurst et al. (2025 preprint).** Probabilistic sensor drift correction and uncertainty-driven calibration scheduling.  
   https://arxiv.org/abs/2506.09186v1

2. **CWSF 2025 top project:** *The Home Smog Alarm: How Clean is Your Home's Air?*  
   https://partner.projectboard.world/ysc/project/the-home-smog-alarm-how-clean-is-your-homes-air

3. **CWSF 2025 Silver project:** *PIONEER: Pipe Inspection and Observation for Non-Destructive Evaluation and Environmental Review.*  
   https://partner.projectboard.world/ysc/project/pioneer-pipe-inspection-and-observation-for-non-destructive-evaluation-and-environmental-review

4. **CWSF 2024 Bronze project:** *Analysis of Toroidal Propeller Sound Characteristics and Efficiency.*  
   https://partner.projectboard.world/ysc/project/analysis-of-toroidal-propeller-sound-characteristics-and-efficiency
