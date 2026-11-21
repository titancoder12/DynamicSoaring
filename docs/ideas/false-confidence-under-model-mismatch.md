# False confidence under model mismatch

**Working question:** Can an information-seeking swarm become confidently wrong?  
**Status:** Strong research architecture; originally shortlisted as candidate B.

## Scientific problem

An informative-sensing planner can reduce the uncertainty of its **own model** while still missing real structure that the model cannot represent. The system may therefore become increasingly confident while its real reconstruction error stays high.

This is a fundamental distinction:

> Low predicted uncertainty is not necessarily low physical error.

## Proposed research question

> Under controlled mismatch between an assumed environmental model and the true field, can a small budget of independent audit measurements detect or reduce false confidence better than pure uncertainty-seeking sampling?

## Proposed hypothesis

Pure uncertainty-driven sampling will perform efficiently on correctly specified smooth fields but can miss unmodelled boundaries or nonstationary structure. Reserving a small fraction of the measurement budget for independent audits may reduce worst-region error and improve uncertainty calibration under mismatch.

A credible null result is that a modern nonstationary or robust baseline already solves the proposed failure.

## Proposed experiment

- Simulate smooth and abrupt scalar fields.
- Use a standard uncertainty-seeking planner.
- Introduce controlled mismatch between the planner's assumed model and the true field.
- Compare:
  - random sampling;
  - uniform sampling;
  - variance-only sampling;
  - a better-specified or nonstationary model;
  - the proposed audit strategy.
- Evaluate:
  - integrated reconstruction error;
  - worst-region error;
  - interval coverage / calibration;
  - resource cost.
- Validate on a separately mapped physical light or temperature field.

## Practical solution path

If the failure is real, the practical system becomes an aerial sensing team that occasionally performs **verification measurements** instead of blindly trusting its own uncertainty map.

This idea can later be specialized to search and rescue, environmental sensing, or airborne mapping.

## Novelty risk

The novelty is **not** uncertainty sampling, active learning, robust Gaussian processes, or nonstationary modelling. The potential contribution must be a precisely characterized failure regime plus a simple diagnostic/remedy that survives comparison with credible modern baselines.

## CWSF-analysis connection

This architecture matches several useful historical patterns:

- Gold AI detector work emphasized shift/calibration rather than headline accuracy.
- Gold astronomy inference focused on distinguishing physical explanations.
- Bronze environmental modelling showed why fitting model-generated labels can mislead.

Relevant internal reports:

- [Candidate architectures](../../reports/analysis/cwsf2027-candidate-architectures.md)
- [Gold vs. Silver/Bronze](../../reports/analysis/gold-vs-silver-bronze.md)
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md)

## References

1. **Krause, Singh & Guestrin (2008).** Gaussian-process sensor placement and mutual information.  
   https://www.jmlr.org/papers/v9/krause08a.html

2. **Sauer, Gramacy & Higdon (2020; revised 2021).** Nonstationary deep-GP surrogate modelling and active learning.  
   https://arxiv.org/abs/2012.08015

3. **Wehbe & Williams (2022).** Resilient/informative planning under uncertainty.  
   https://arxiv.org/abs/2206.11789

4. **CWSF 2024 project:** *Can We Trust AI Text Detectors? Exposing Limitations and Proposing Fixes.*  
   https://partner.projectboard.world/ysc/project/can-we-trust-ai-text-detectors-exposing-limitations-and-proposing-fixes

5. **CWSF 2026 project:** *Ghosts in the Stream: Probing Dark Matter in the GD-1 Stellar Stream with Simulation-Based Inference.*  
   https://partner.projectboard.world/ysc/project/ghosts-in-the-stream-probing-dark-matter-in-the-gd-1-stellar-stream-with-simulation-based-inference

6. **CWSF 2025 project:** *Assessing the Impacts of Climate Change on Lake Winnipeg's Evaporation Using Neural Network Models.*  
   https://partner.projectboard.world/ysc/project/assessing-the-impacts-of-climate-change-on-lake-winnipegs-evaporation-using-neural-network-models
