# Delayed communication tradeoff

**Working question:** When is communication worth its cost?  
**Status:** Conditional swarm-focused architecture; originally candidate A.

## Scientific problem

Shared observations can become stale before another agent acts on them. Communication also costs time, energy, bandwidth, rendezvous travel, or computation.

The question is not whether communication is useful in principle. It is:

> When does sharing improve the actual scientific/task outcome enough to justify its cost?

## Proposed research question

> How does the ratio between communication delay and environmental-change timescale affect whether cooperation improves independently measured field error at a fixed total resource budget?

## Proposed hypothesis

Communication helps when shared measurements remain fresh relative to the environment. As the field changes faster or messages arrive later, cooperation can become neutral or harmful unless the planner accounts for information freshness.

## Proposed experiment

- Simulated agents sampling a time-varying scalar field.
- Vary:
  - communication delay;
  - packet loss;
  - environmental timescale;
  - team size.
- Compare:
  - no sharing;
  - periodic sharing;
  - independent greedy sampling;
  - centralized planning;
  - freshness-aware sharing;
  - a relevant published stale-belief baseline.
- Measure:
  - actual map error;
  - interval coverage;
  - distance / energy proxy;
  - message count;
  - wall-clock cost.

Physical validation could replay a changing light/temperature field with two sensors and measured network latency.

## Practical solution path

The result could guide when a flying swarm should exchange observations, continue independently, or rendezvous.

Possible applications include:

- search-and-rescue teams;
- environmental monitoring;
- cooperative gliders;
- atmospheric sensing.

## Novelty risk

Recent research directly addresses stale decentralized beliefs and adaptive communication windows. A generic “communication-aware swarm” is not a credible novelty claim.

The contribution would need a narrower, experimentally verified result under a specific physical sensing problem or cost structure.

## CWSF-analysis connection

The historical review highlighted a Silver multi-agent traffic project that explicitly removed communication while keeping evaluation flows shared. This supports the value of a clear counterfactual, but does not show that communication itself predicts medals.

## References

1. **Wehbe & Williams (2022).** Informative planning under uncertain/unreliable communication.  
   https://arxiv.org/abs/2206.11789

2. **Cao et al. (2026 preprint).** Spatiotemporal field belief, stale information, decentralized belief exchange and conservative fusion.  
   https://arxiv.org/abs/2609.05515v1

3. **Rossano, Lim & How (2026 preprint).** Adaptive communication windows / rendezvous cost during exploration.  
   https://arxiv.org/abs/2609.12502v1

4. **CWSF 2021 Silver project:** *Multi-Agent AI System for Emergency Vehicle Preemption.*  
   https://partner.projectboard.world/ysc/project/multi-agent-ai-system-for-emergency-vehicle-preemption

5. **CWSF 2021 Bronze project:** *Wildfire Drone Automation Using Deep Learning.*  
   https://partner.projectboard.world/ysc/project/wildfire-drone-automation-using-deep-learning-zjmwy
