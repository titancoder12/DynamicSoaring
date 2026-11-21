# Literature Review and Novelty Assessment — Wind-Adaptive Fixed-Wing Swarms

**Date:** 2026-10-18  
**Status:** Preliminary, source-backed literature scan; not a systematic review or proof of novelty.  
**Related concept:** [Wind-Adaptive Decentralized Fixed-Wing Swarms](../ideas/wind-adaptive-decentralized-fixed-wing-swarms.md)

## Executive finding
Distributed RL, fixed-wing formation control, disturbance rejection, and communication reduction are all established research areas. A generic combination of these is **not** a defensible novelty claim. A narrower candidate is **cooperative reconstruction of spatially varying wind from each aircraft's partial observations, under a constrained communication budget, to improve formation robustness**. This is a *hypothesis about a possible gap*, not confirmed new science.

## Source-by-source novelty matrix

| Source | Established contribution | Implication / unresolved verification |
|---|---|---|
| Liu et al., *Robust optimal formation control for fixed-wing UAVs with external disturbances via reinforcement learning: Theory and experiment* (Aerospace Science and Technology, 2026), DOI: 10.1016/j.ast.2026.112884 | Distributed robust RL control under disturbances, with fixed-wing flight experiments | Rules out generic “RL + fixed-wing formation + wind robustness” as novel. Inspect full paper for explicit sharing of spatial wind estimates. |
| *Event triggered formation tracking control of fixed wing UAV swarm Based on Improved Reinforcement Learning* (2026), DOI: 10.7527/S1000-6893.2026.33171 | Event-triggered distributed observation, RL, wind-disturbance compensation, reduced communication | Rules out generic “wind + RL + bandwidth efficiency” novelty; compare transmitted state versus environmental estimates. |
| *Distributed robust adaptive practical finite-time formation tracking control of fixed-wing UAVs* (Aerospace Science and Technology, 2025), DOI: 10.1016/j.ast.2025.110552 | Distributed adaptive formation tracking with wind and aerodynamic uncertainties | Classical adaptive control is a strong non-RL baseline. |
| *Adaptive optimal control for distributed fixed-wing UAV formations: Integration of predefined-time convergence and actor-critic learning* (Neurocomputing, 2026), DOI: 10.1016/j.neucom.2025.132106 | Actor-critic adaptive formation control under disturbances | Learning alone is not novel; consider explicit wind-field estimation and information-sharing interventions. |
| Li et al., *A Review of Fixed-Wing Unmanned Aerial Vehicle Formation Research* (2026), DOI: 10.62762/AEC.2025.339037 | Reviews architectures, topology, control, navigation, energy and communications | Use bibliography to expand search and identify strong baselines. |
| Zhu et al., *A survey of multi-agent deep reinforcement learning with communication* (2024), DOI: 10.1007/s10458-023-09633-6 | Communication in MARL is established | Learned messages are not by themselves a novelty claim. |
| Ekechi et al., *A Survey on UAV Control with Multi-Agent Reinforcement Learning* (Drones, 2025), DOI: 10.3390/drones9070484 | Surveys MARL for UAV control | Distinguish fixed-wing dynamics from generic quadrotor abstractions. |

## Proposed scientific question
**Under what spatial and temporal wind-correlation conditions does sharing compact, uncertain wind estimates between decentralized fixed-wing UAVs reduce formation tracking error or safety violations relative to equally bandwidth-limited state-only communication?**

This is intentionally falsifiable: sharing may be harmful if wind fields are uncorrelated, estimates are stale, or latency is excessive.

## Candidate hypotheses
- H1: In spatially correlated but heterogeneous wind, shared local wind estimates improve formation tracking over matched-bandwidth state-only messages.
- H2: The benefit diminishes or reverses as wind correlation length falls or communication delay rises.
- H3: Confidence-weighted, event-triggered messages can preserve most of the benefit while reducing bytes transmitted compared with fixed-rate sharing.

## Fair comparison plan
Hold flight dynamics, controller capacity, sensor inputs, compute, training budget, random seeds, and communication-byte budget constant where applicable.
1. Conventional distributed formation controller with local disturbance observer.
2. Independent adaptive controller with no inter-agent messages.
3. Decentralized MARL with state-only messages.
4. Decentralized MARL with wind-estimate messages.
5. Same as (4) but confidence-weighted / event-triggered.
6. Oracle global wind field (upper bound only, not deployable baseline).

Separate *estimation* from *control*: evaluate wind-field reconstruction accuracy even if formation performance does not improve. For communication comparisons, count payload, headers, update frequency, retransmissions if modeled, and latency. Include a simple non-RL cooperative wind-estimation baseline to determine whether learning is needed.

## Experimental variables
- Independent: wind spatial correlation length, gust intensity, temporal decorrelation, team size (2/3/5/8), neighbor radius, packet loss, delay, sensor noise and model mismatch.
- Primary dependent: RMS relative-position formation error and minimum separation / safety violation frequency.
- Secondary: wind estimation RMSE, recovery time, energy/control-effort proxy, bytes per agent-second, runtime.
- Controls: fixed-wing stall speed, bank/turn limits, identical initial conditions and matched compute and communication budgets.
- Statistical plan: paired wind-field seeds, multiple training seeds, held-out wind distributions, confidence intervals and negative-result reporting. Predefine one primary endpoint before the final study.

## Technical risks and mitigations
- **Novelty overlap:** review full texts and citations specifically for cooperative wind-field estimation before asserting originality.
- **Simulator artifacts:** validate wind models and aircraft dynamics; run model mismatch sweeps and hardware-in-loop.
- **Reward hacking:** use hard safety constraints, not just reward penalties.
- **Overambitious hardware:** start with single FW-01 ground/flight validation, not simultaneous multi-aircraft outdoor operations.
- **Unmeasured energy:** label control effort as a proxy until electrical power is measured and calibrated.
- **Previous-project overlap:** clearly distinguish this project's wind-information estimation and fixed-wing physics from prior ground swarm MARL work.

## Feasibility gate (next 2–3 weeks)
1. Read the full texts of the two closest 2026 studies; extract exact observation/action spaces, message contents, wind models and baseline metrics.
2. Search explicitly for distributed/cooperative wind-field estimation, atmospheric mapping with UAV teams, and belief sharing under bandwidth constraints; add closest papers.
3. Implement a small 2-D fixed-wing kinematic model with wind and turn-rate constraints, a spatially correlated stochastic wind field, and a simple non-RL distributed controller.
4. Compare state-only vs shared-wind messages under equal bandwidth. If the effect is negligible, pivot before implementing MARL.
5. Only then consider a higher-fidelity simulator and RL.

## Decision
**Conditional GO for a low-cost simulation feasibility study; NOT YET GO for full CWSF commitment.** The literature supports relevance, but originality remains unverified. A rigorous negative finding about when cooperation fails could also be scientifically useful.

## Links
- https://doi.org/10.1016/j.ast.2026.112884
- https://hkxb.buaa.edu.cn/EN/10.7527/S1000-6893.2026.33171
- https://doi.org/10.1016/j.ast.2025.110552
- https://doi.org/10.1016/j.neucom.2025.132106
- https://doi.org/10.62762/AEC.2025.339037
- https://doi.org/10.1007/s10458-023-09633-6
- https://doi.org/10.3390/drones9070484
