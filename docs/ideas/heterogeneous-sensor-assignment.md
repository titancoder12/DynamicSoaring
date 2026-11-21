# Heterogeneous sensor assignment

**Working question:** Which sensor should measure next?  
**Status:** Candidate architecture G; likely extension rather than first project.

## Scientific problem

A distributed team may contain many fast/noisy sensors and a few slower/more accurate sensors. Treating every observation as equally valuable wastes the team's diversity.

## Proposed research question

> When does adaptive assignment of sensor quality outperform fixed specialist roles under equal total time and energy?

## Proposed hypothesis

Using high-quality sensors only in ambiguous regions can improve inference when confirmation cost is moderate, but fixed roles may win when travel, latency or sensing cost dominates.

## Proposed experiment

Simulate two sensor classes, then validate with two real sensors or controlled noise modes.

Vary:

- noise ratio;
- sensing latency;
- travel cost;
- team composition.

Measure:

- reconstruction error;
- calibration;
- energy/time;
- confirmation frequency.

Compare:

- fixed assignments;
- round-robin;
- uncertainty-only dispatch;
- cost-aware dispatch;
- homogeneous-team condition.

## Practical solution path

A flying team could combine:

- wide-area, low-cost cameras;
- high-resolution or thermal confirmation sensors;
- fast scouts and slower confirmers.

The research question should be about **when specialization is worth its cost**, not merely demonstrating heterogeneous hardware.

## Novelty risk

Multi-robot planning with varied sensor types already has substantial prior art. This is best retained as an extension unless a strong unexplored resource-allocation question is identified.

## CWSF-analysis connection

The historical analysis includes:

- Silver sensor-fusion comparisons;
- Bronze physical tradeoff experiments;
- Gold measurement systems.

The key lesson is to isolate the value of sensor heterogeneity rather than attributing gains to a larger or more expensive system.

## References

1. **Jakkala & Akella (2026).** Differentiable sensor placement and multi-robot planning with diverse sensor types.  
   https://journals.sagepub.com/doi/10.1177/02783649251384993

2. **CWSF 2025 Silver project:** *PIONEER.*  
   https://partner.projectboard.world/ysc/project/pioneer-pipe-inspection-and-observation-for-non-destructive-evaluation-and-environmental-review

3. **CWSF 2024 Bronze project:** *Analysis of Toroidal Propeller Sound Characteristics and Efficiency.*  
   https://partner.projectboard.world/ysc/project/analysis-of-toroidal-propeller-sound-characteristics-and-efficiency

4. **CWSF 2023 Gold project:** *Auto-Pend Lab.*  
   https://partner.projectboard.world/ysc/project/auto-pend-lab-jzrgnd
