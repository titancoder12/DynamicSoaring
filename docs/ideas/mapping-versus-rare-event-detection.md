# Mapping versus rare-event detection

**Working question:** Should a sensing swarm map everything well, or find rare changes quickly?  
**Status:** Candidate architecture E.

## Scientific problem

A policy that minimizes average map error can still miss a brief, localized event. Conversely, a system optimized for anomaly detection may produce a poor general map.

This creates a direct tension between:

- global reconstruction quality;
- rapid rare-event detection.

## Proposed research question

> How does allocating measurements between global mapping and change detection affect detection delay at a controlled false-alarm rate?

## Proposed hypothesis

A mixed policy will reduce detection delay for rare localized events at the cost of some average mapping accuracy. The preferred balance should depend on event duration, size and background variability.

## Proposed experiment

Use a controlled light or temperature field.

Vary:

- event duration;
- event size;
- background variability;
- mapping/detection objective weight.

Measure:

- detection delay;
- missed events;
- false alarms;
- map error.

Compare:

- uniform revisit;
- uncertainty-only mapping;
- change-triggered sampling;
- mixed objective.

Use previously unseen event shapes/rates for final testing and fix detection thresholds before final evaluation.

## Practical solution path

This architecture can be mapped naturally onto:

- wildfire detection;
- search-and-rescue target detection;
- pollution leaks;
- ecological anomalies;
- thermal hotspots.

For SAR, the scientific question becomes whether maximizing coverage can actually delay discovery of a rare target.

## Novelty risk

Adaptive monitoring and anomaly detection are established. The contribution must be a carefully measured tradeoff or decision boundary for a specific sensing regime, not simply a two-objective planner.

## CWSF-analysis connection

The repo's historical analysis repeatedly warns against optimizing a convenient proxy. A beautiful map is not automatically a good detector, just as high model confidence is not automatically correct inference.

## References

1. **CWSF 2024 Gold project:** *Can We Trust AI Text Detectors? Exposing Limitations and Proposing Fixes.*  
   https://partner.projectboard.world/ysc/project/can-we-trust-ai-text-detectors-exposing-limitations-and-proposing-fixes

2. **CWSF 2026 Bronze project:** *Firebird: Autonomous UAV Detection and Monitoring of Wildfires.*  
   https://partner.projectboard.world/ysc/project/firebird-autonomous-uav-detection-and-monitoring-of-wildfires

3. **CWSF 2025 Platinum project:** *The Home Smog Alarm: How Clean is Your Home's Air?*  
   https://partner.projectboard.world/ysc/project/the-home-smog-alarm-how-clean-is-your-homes-air

4. **Hollinger & Sukhatme (2014).** Resource-bounded robotic information gathering.  
   https://journals.sagepub.com/doi/10.1177/0278364914533443
