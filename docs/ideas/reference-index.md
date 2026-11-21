# Reference index for CWSF 2027 idea library

This index consolidates the external and internal references cited across the idea documents. Individual idea notes retain their own focused reference lists; this file makes cross-idea prior art easier to audit.

## Informative sensing / active measurement

1. **Krause, A., Singh, A., & Guestrin, C. (2008).** Near-optimal sensor placements in Gaussian processes: mutual information and robust placement. JMLR.  
   https://www.jmlr.org/papers/v9/krause08a.html  
   Used by: information-foraging, false-confidence, atmospheric profiling, model-discrimination.

2. **Singh, A., Krause, A., Guestrin, C., & Kaiser, W. (2009).** Efficient informative sensing using multiple robots. JAIR.  
   https://arxiv.org/abs/1401.3462  
   Used by: information-foraging, atmospheric profiling.

3. **Hollinger, G., & Sukhatme, G. (2014).** Sampling-based robotic information gathering algorithms. IJRR.  
   https://journals.sagepub.com/doi/10.1177/0278364914533443  
   Used by: information-foraging, rare-event/mapping tradeoff.

4. **Cao, N., Low, K. H., & Dolan, J. (2013 preprint).** Multi-robot informative planning / active sensing.  
   https://arxiv.org/abs/1302.0723  
   Used by: information-foraging.

5. **Sauer, A., Gramacy, R., & Higdon, D. (2020; revised 2021).** Nonstationary deep-GP surrogate modelling and active learning.  
   https://arxiv.org/abs/2012.08015  
   Used by: false-confidence under model mismatch.

6. **Wehbe, R., & Williams, B. (2022).** Informative planning with unreliable shared information / communication uncertainty.  
   https://arxiv.org/abs/2206.11789  
   Used by: information-foraging, false-confidence, delayed communication.

7. **Jakkala, K., & Akella, S. (2026).** Differentiable sensor placement / multi-robot path planning with diverse sensor types. IJRR.  
   https://journals.sagepub.com/doi/10.1177/02783649251384993  
   Used by: information-foraging, heterogeneous sensors.

8. **Cao et al. (2026 preprint).** Spatiotemporal field belief, stale decentralized information and conservative fusion.  
   https://arxiv.org/abs/2609.05515v1  
   Used by: information-foraging, delayed communication.

9. **Rossano, Lim & How (2026 preprint).** Adaptive communication windows / rendezvous cost during exploration.  
   https://arxiv.org/abs/2609.12502v1  
   Used by: information-foraging, delayed communication.

10. **Hurst et al. (2025 preprint).** Probabilistic drift correction and uncertainty-driven calibration scheduling.  
    https://arxiv.org/abs/2506.09186v1  
    Used by: recalibration versus exploration.

## Active perception and aerial search

11. **Velez et al. (2012).** Active perception planning with correlated detections from nearby viewpoints. JAIR.  
    https://jair.org/index.php/jair/article/view/10770  
    Used by: cooperative aerial search.

12. **Schedl, D. C., Kurmi, I., & Bimber, O. (2020).** Search and rescue with airborne optical sectioning. Nature Machine Intelligence.  
    https://www.nature.com/articles/s42256-020-00261-3  
    Used by: cooperative aerial search, flying camera array.

13. **Schedl, Kurmi & Bimber (2021).** Autonomous Drones for Search and Rescue in Forests. Science Robotics.  
    https://doi.org/10.1126/scirobotics.abg1188  
    Used by: cooperative aerial search, flying camera array.

14. **Kurmi et al. (2022).** Through-Foliage Tracking with Airborne Optical Sectioning. Journal of Remote Sensing.  
    https://spj.science.org/doi/10.34133/2022/9812765  
    Used by: flying camera array.

15. **Kurmi / Bimber group (2022).** On the Role of Field of View for Occlusion Removal with Airborne Optical Sectioning.  
    https://arxiv.org/abs/2204.13371  
    Used by: flying camera array.

16. **Nathan, Kurmi & Bimber (2023).** Drone swarm strategy for the detection and tracking of occluded targets in complex environments. Nature Communications Engineering.  
    https://www.nature.com/articles/s44172-023-00104-0  
    Used by: cooperative aerial search, flying camera array.

17. **Nathan & Bimber (2023).** Synthetic Aperture Anomaly Imaging for Through-Foliage Target Detection. Remote Sensing.  
    https://arxiv.org/abs/2304.13590  
    Used by: flying camera array.

18. **Pöschl (2023).** Adaptive Particle Swarm Optimization for through-foliage target detection with drone swarms.  
    https://arxiv.org/abs/2310.10320  
    Used by: flying camera array.

19. **Nathan et al. (2024).** Reciprocal Visibility for Guided Occlusion Removal With Drones. IEEE GRSL.  
    https://arxiv.org/abs/2402.06991  
    Used by: cooperative aerial search, flying camera array.

20. **Nathan et al. (2025).** An Autonomous Drone Swarm for Detecting and Tracking Anomalies among Dense Vegetation. Nature Communications Engineering.  
    https://www.nature.com/articles/s44172-025-00546-8  
    Used by: cooperative aerial search, flying camera array.

21. **Youssef & Bimber (2025).** DeepForest: Sensing Into Self-Occluding Volumes of Vegetation With Aerial Imaging. Journal of Remote Sensing.  
    https://spj.science.org/doi/10.34133/remotesensing.0907  
    Used by: flying camera array.

22. **Next Best View planning for occluded UAV search (2025 preprint).**  
    https://arxiv.org/html/2511.18353v1  
    Used by: cooperative aerial search.

23. **Youssef et al. (2026).** Through-Foliage Surface-Temperature Reconstruction for Early Wildfire Detection. Nature Communications AI & Computing.  
    https://www.nature.com/articles/s44488-026-00012-0  
    Used by: flying camera array.

24. **Nathan et al. (2026).** Aerial color image anomaly dataset for search missions in complex forested terrain. Nature Scientific Data.  
    https://www.nature.com/articles/s41597-026-07101-w  
    Used by: cooperative aerial search, flying camera array.

25. **ForestPersons (2026).** Missing-person detection dataset/paper for forested environments.  
    https://arxiv.org/html/2603.02541v1  
    Dataset: https://huggingface.co/datasets/etri/ForestPersons  
    Used by: cooperative aerial search.

26. **JKU Airborne Optical Sectioning repository.** Code, data, simulations and swarm resources.  
    https://github.com/JKU-ICG/AOS  
    Used by: cooperative aerial search, flying camera array.

27. **Crazyswarm2.** Multi-quadrotor research platform.  
    https://imrclab.github.io/crazyswarm2/  
    Used by: cooperative aerial search implementation planning.

## Fixed-wing flight and soaring

28. **NASA Glenn Research Center.** Lift to Drag Ratio.  
    https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/lift-to-drag-ratio/  
    Used by: fixed-wing autonomous search.

29. **ArduPilot Plane — AUTO mode.**  
    https://ardupilot.org/plane/docs/auto-mode.html  
    Used by: fixed-wing autonomous search.

30. **ArduPilot Plane — Soaring.**  
    https://ardupilot.org/plane/docs/soaring.html  
    Used by: fixed-wing autonomous search, cooperative thermal soaring.

31. **Tabor, Guilliard & Kolobov (2018).** ArduSoar: an Open-Source Thermalling Controller for Resource-Constrained Autopilots.  
    https://arxiv.org/abs/1802.08215  
    Used by: fixed-wing autonomous search, cooperative thermal soaring.

32. **Flato et al. (2024).** Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement learning. Nature Communications.  
    https://doi.org/10.1038/s41467-024-48670-x  
    Used by: fixed-wing autonomous search, cooperative thermal soaring.

33. **Mohamadi & Kara (2026).** SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders.  
    https://arxiv.org/abs/2602.12838  
    Full text: https://arxiv.org/html/2602.12838v1  
    Used by: fixed-wing autonomous search, cooperative thermal soaring.

## Acoustic search

34. **DroneAudioset (2025).** Drone-recorded SAR audio dataset / NeurIPS 2025 Datasets and Benchmarks work.  
    https://arxiv.org/abs/2510.15383  
    Used by: distributed acoustic search.

## Flight rules and safety

35. **Transport Canada.** Learn the rules before you fly your drone.  
    https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone  
    Used by: cooperative aerial search, acoustic search, fixed-wing search, thermal soaring.

## CWSF historical anchors used in idea design

36. **Active-control rocket — Platinum.**  
    https://partner.projectboard.world/ysc/project/an-investigation-into-active-control-for-accessible-orbital-flight

37. **Multi-Agent AI System for Emergency Vehicle Preemption — Silver.**  
    https://partner.projectboard.world/ysc/project/multi-agent-ai-system-for-emergency-vehicle-preemption

38. **Wildfire Drone Automation Using Deep Learning — Bronze.**  
    https://partner.projectboard.world/ysc/project/wildfire-drone-automation-using-deep-learning-zjmwy

39. **Can We Trust AI Text Detectors? — Gold.**  
    https://partner.projectboard.world/ysc/project/can-we-trust-ai-text-detectors-exposing-limitations-and-proposing-fixes

40. **Ghosts in the Stream / GD-1 dark-matter inference — Gold.**  
    https://partner.projectboard.world/ysc/project/ghosts-in-the-stream-probing-dark-matter-in-the-gd-1-stellar-stream-with-simulation-based-inference

41. **Home Smog Alarm — Platinum.**  
    https://partner.projectboard.world/ysc/project/the-home-smog-alarm-how-clean-is-your-homes-air

42. **PIONEER — Silver.**  
    https://partner.projectboard.world/ysc/project/pioneer-pipe-inspection-and-observation-for-non-destructive-evaluation-and-environmental-review

43. **Toroidal Propeller study — Bronze.**  
    https://partner.projectboard.world/ysc/project/analysis-of-toroidal-propeller-sound-characteristics-and-efficiency

44. **Stratosync — Silver.**  
    https://partner.projectboard.world/ysc/project/stratosync

45. **Firebird wildfire UAV — Bronze.**  
    https://partner.projectboard.world/ysc/project/firebird-autonomous-uav-detection-and-monitoring-of-wildfires

46. **Auto-Pend Lab — Gold.**  
    https://partner.projectboard.world/ysc/project/auto-pend-lab-jzrgnd

47. **Lake Winnipeg evaporation model — Bronze.**  
    https://partner.projectboard.world/ysc/project/assessing-the-impacts-of-climate-change-on-lake-winnipegs-evaporation-using-neural-network-models

48. **Ca II absorber catalogue — Gold.**  
    https://partner.projectboard.world/ysc/project/probing-galaxy-disk-sizes-using-the-largest-ever-catalog-of-ca-ii-absorbers

49. **BL Lacertae light-echo model — Silver.**  
    https://partner.projectboard.world/ysc/project/modelling-the-light-echo-in-active-galaxy-bl-lacertae-using-high-cadence-light-curve-data

## Rocket-assisted glider launch

Added for [Rocket-assisted launch for autonomous gliders](rocket-assisted-glider-launch.md), documented 2026-09-21. These five additional sources, together with existing entries **30** (ArduPilot Soaring) and **35** (Transport Canada), retain all seven references from the rocket-glider discussion. Relevant public text was checked on 2026-09-21; the concept note records the inspection scope and limitations. NAR competition/safety references are not Canadian flight authorization.

50. **National Association of Rocketry.** Radio Control Rocket Glider Safety Code.  
    https://www.nar.org/content.aspx?club_id=114127&module_id=669240&page_id=22  
    Used by: rocket-assisted glider launch. Radio-controlled precedent and boost/glide flightworthiness; the hosted code is marked January 1998.

51. **National Association of Rocketry.** NARAM-68 Boost Glide Duration.  
    https://nar.org/content.aspx?club_id=114127&module_id=796415&page_id=22  
    Used by: rocket-assisted glider launch. Overview of a gliding portion and separately recovered motor pod.

52. **National Association of Rocketry.** S4—Boost Glider.  
    https://www.nar.org/content.aspx?club_id=114127&module_id=674283&page_id=22  
    Used by: rocket-assisted glider launch. Retained-component gliding precedent and transition/lift/recovery challenges; the competition example is free-flight, not autonomous search.

53. **Government of Canada, Justice Laws Website.** Canadian Aviation Regulations, SOR/96-433, sections 602.43–602.45.  
    https://laws-lois.justice.gc.ca/eng/regulations/sor-96-433/page-59.html  
    Used by: rocket-assisted glider launch. Rocket authorization and aviation-safety provisions; the proposed combined vehicle still requires operation-specific classification/review.

54. **Canadian Association of Rocketry / Association canadienne de fuséonautique.** Model Rocketry Safety Code.  
    https://www.canadianrocketry.org/en/regulations/model-rocketry  
    Used by: rocket-assisted glider launch. Approved motors, recovery, site permission, and preflight checks; not a substitute for applicable law.

## Humanitarian civilian-protection concept references — 2026-10-18

Sources below support the four new [humanitarian protection idea notes](search-for-safety-humanitarian-aerial-intelligence.md). Titles and scientific background were checked at abstract/institutional-page level, not full-methods replication. The documentary is user-supplied inspiration, not an independently reviewed transcript. These are not novelty proofs.

- **Original documentary:** https://www.youtube.com/watch?v=CyA9s4MEwnw — inspiration for fixed-wing drone observation, civilian route assessment and defensive warning.
- **UN HRMMU (26 June 2025),** *Deadly Drones: Civilians at Risk from Short-Range Drones* — historic casualty context with explicit February 2022–April 2025 window. https://ukraine.ohchr.org/en/Deadly-drones-Civilians-at-risk-from-short-range-drones-in-frontline-areas-of-Ukraine-24-February-2022-30-April-2025
- **ICRC (2022),** *How humanitarian corridors work* — humanitarian corridors require agreements and remain hazardous. https://www.icrc.org/en/document/how-humanitarian-corridors-work
- **Nguyen & Akella (2026),** *Dynamic UGV-UAV Cooperative Path Planning in Uncertain Environments* — existing UAV/road inspection baseline. https://arxiv.org/abs/2604.25267
- **Choi et al. (2026),** *Integrated Exploration-Aware UAV Route Optimization and Path Planning* — existing uncertain-hazard and reinspection planning. https://arxiv.org/abs/2605.28654
- **Han et al. (2023),** disaster crowdsensing route planning. https://arxiv.org/abs/2308.11088
- **Isaac-Medina et al. (2021),** visual UAV detection and tracking benchmark. https://openaccess.thecvf.com/content/ICCV2021W/AntiUAV/html/Isaac-Medina_Unmanned_Aerial_Vehicle_Visual_Detection_and_Tracking_Using_Deep_Neural_ICCVW_2021_paper.html
- **Jiang et al. (2021),** Anti-UAV benchmark. https://arxiv.org/abs/2101.08466
- **Drone-vs-Bird challenge,** benign false-positive benchmark; check usage permission. https://github.com/wosdetc/challenge
- **ISED Canada,** jammer prohibitions including RF counter-drone devices. https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/safety-and-compliance/compliance-and-enforcement/jammers-are-prohibited-canada-thats-law
- **ISED Canada,** drone detection receiver/scanning compliance guidance. https://ised-isde.canada.ca/site/certification-engineering-bureau/en/notice-2024-drs0010
- **Transport Canada,** drone operating rules. https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone

## Bio-inspired flight and adaptive soaring — consolidated research papers (2026-10-18)

This section brings together the papers discussed for the AI-powered adaptive dynamic-soaring project and adjacent bio-inspired flight ideas. **Primary annotated bibliography:** [AI-powered adaptive dynamic soaring — papers and engineering references](../projects/ai-powered-adaptive-dynamic-soaring/06-annotated-references.md). **Project dossier:** [AI-powered adaptive dynamic soaring](../projects/ai-powered-adaptive-dynamic-soaring/README.md). These are references for learning, reproducing published experiments, and benchmarking—not claims of original novelty or validated FW-01 performance. Thermal soaring and dynamic soaring are distinct physical mechanisms.

### A. Albatross dynamic-soaring physics and observed flight

55. **Richardson, P. L. (2015).** *Upwind dynamic soaring of albatrosses and UAVs.* Progress in Oceanography **130**, 146–156.  
    https://doi.org/10.1016/j.pocean.2014.11.002  
    **Use:** Wind-shear flight cycles, upwind tacking-like trajectories and a two-layer robotic-albatross model. Inferred UAV speeds are idealized theoretical predictions, not demonstrated physical performance.

56. **Sachs, G. (2005).** *Minimum shear wind strength required for dynamic soaring of albatrosses.* Ibis **147**, 1–10.  
    https://doi.org/10.1111/j.1474-919x.2004.00295.x  
    **Use:** Shear thresholds and whether small aircraft with a given drag polar can sustain energy-neutral cycles.

57. **Deittert, M., Richards, A., Toomer, C. A., & Pipe, A. (2009).** *Engineless unmanned aerial vehicle propulsion by dynamic soaring.* Journal of Guidance, Control, and Dynamics **32**(5), 1446–1457.  
    https://doi.org/10.2514/1.43270  
    **Use:** Classical soaring trajectories, equations and simulation baselines.

58. **Sachs, G. (2016).** *In-flight measurement of upwind dynamic soaring in albatrosses.* Progress in Oceanography **142**, 47–57.  
    https://doi.org/10.1016/j.pocean.2016.01.003  
    **Use:** GPS-based observations and analysis of real albatross upwind flight. Directly supports comparison between large-scale bird flight and a sailing boat's tacking pattern.

59. **Richardson, P. L., Wakefield, E. D., & Phillips, R. A. (2018).** *Flight speed and performance of the wandering albatross with respect to the wind.* Movement Ecology **6**.  
    https://doi.org/10.1186/s40462-018-0121-9  
    **Use:** Field-observation benchmark for wind-relative bird flight.

60. **Richardson, P. L., & Wakefield, E. D. (2022).** *Observations and models of across-wind flight speed of the wandering albatross.* Royal Society Open Science **9**, 211364.  
    https://doi.org/10.1098/rsos.211364  
    **Use:** Across-wind flight-speed observations and model comparisons.

### B. AI, neural feedback and reinforcement learning for dynamic soaring

61. **Kim, S.-h., Lee, J., Jung, S., Lee, H., & Kim, Y. (2019).** *Deep neural network-based feedback control for dynamic soaring of unpowered aircraft.* IFAC-PapersOnLine **52**(12), 117–121.  
    https://doi.org/10.1016/j.ifacol.2019.11.079  
    **Use:** Initial neural-feedback architecture based on optimized soaring trajectories.

62. **Zou, W., Li, N., An, F., Wang, K., & Dong, C. (2025).** *A novel trajectories optimizing method for dynamic soaring based on deep reinforcement learning.* Defence Technology **46**, 99–108.  
    https://doi.org/10.1016/j.dt.2024.12.007  
    **Use:** PPO-based soaring trajectory optimization and a classical nonlinear optimization comparator.

63. **Lu, Y., Xie, F., & Ji, T. (2025).** *Human-in-the-loop reinforcement learning for dynamic soaring: A trajectory planning and control integrated system.* Engineering Applications of Artificial Intelligence **157**, 111219.  
    https://doi.org/10.1016/j.engappai.2025.111219  
    **Use:** Connecting learned trajectory planning to low-level flight control.

64. **Sun, S., Shao, Z., Xu, X., & Zhou, Z. (2026).** *Enhancing UAV endurance: coupled optimization of dynamic soaring trajectory and high-fidelity powertrain energy management.* Applied Energy **416**, 127955.  
    https://doi.org/10.1016/j.apenergy.2026.127955  
    **Use:** Account for battery, ESC, motor and propeller when evaluating full-mission energy savings. Do not treat its published improvement as a prediction for FW-01.

### C. Thermal soaring and engineering implementation (different physical mechanism)

65. **Reddy, G., Wong-Ng, J., Celani, A., Sejnowski, T. J., & Vergassola, M. (2018).** *Glider soaring via reinforcement learning in the field.* Nature **562**, 236–239.  
    https://doi.org/10.1038/s41586-018-0533-0  
    **Use:** Real-world reinforcement-learning controlled thermal soaring, as an adjacent autopilot and field-validation reference.

- **Flato et al. (2024).** *Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* Nature Communications. https://doi.org/10.1038/s41467-024-48670-x. **Already listed as #32.** Use for bird-inspired RL thermalling, not albatross wind-shear energy extraction.
- **Tabor, Guilliard & Kolobov (2018).** *ArduSoar: an open-source thermalling controller for resource-constrained autopilots.* https://arxiv.org/abs/1802.08215. **Already listed as #31.** Use as practical ArduPilot thermal-centering reference.

### D. Morphing wings and other biological flight mechanisms

66. **Lentink, D., et al. (2007).** *How swifts control their glide performance with morphing wings.* Nature **446**, 1082–1085.  
    https://doi.org/10.1038/nature05733  
    **Use:** Experimental wing-sweep geometry and aerodynamic trade-offs.

67. **Jeger, F., et al. (2024).** *Adaptive morphing of wing and tail for stable, resilient, and energy-efficient flight of avian-inspired drones.* npj Robotics **2**, 8.  
    https://doi.org/10.1038/s44182-024-00015-y  
    **Use:** Hardware demonstration of bird-inspired shape-changing flight control and energy evaluation.

68. **Weimerskirch, H., et al. (2016).** *Frigate birds track atmospheric conditions over months-long transoceanic flights.* Science **353**, 74–78.  
    https://doi.org/10.1126/science.aaf4374  
    **Use:** Atmospheric energy-aware flight behavior, including uplift exploitation.

69. **Tucker, V. A. (1995).** *Drag reduction by wing tip slots in a gliding Harris' hawk.* Journal of Experimental Biology **198**, 775–781.  
    https://doi.org/10.1242/jeb.198.3.775  
    **Use:** Bird-feather-inspired wingtip aerodynamics.

70. **Miklosovic, D. S., Murray, M. M., Howle, L. E., & Fish, F. E. (2004).** *Leading-edge tubercles delay stall on humpback whale flippers.* Physics of Fluids **16**, L39–L42.  
    https://doi.org/10.1063/1.1688341  
    **Use:** Whale-flipper-inspired stall and lift experiments on finite wings.

71. **Cummins, C., et al. (2018).** *A separated vortex ring underlies the flight of the dandelion.* Nature **562**, 414–418.  
    https://doi.org/10.1038/s41586-018-0604-2  
    **Use:** Passive airborne sensor/seed dispersal aerodynamics.

For more ideas and references on owl silent flight, dragonfly corrugated wings, insect optic-flow sensing and maple samaras, see [Bio-inspired flight engineering options](bio-inspired-flight-research-options-2026-10-18.md). Where a primary citation has not been verified, it is identified as a research lead rather than assigned a fabricated bibliographic entry.

### Suggested reading order for student engineering work

1. **Physics first:** #56 (Sachs 2005) and #57 (Deittert 2009).
2. **Bird flight mechanism:** #55 (Richardson 2015) and #58 (Sachs 2016).
3. **First neural controller:** #61 (Kim 2019).
4. **Train reinforcement-learning baseline:** #62 (Zou 2025).
5. **Integrate planning with flight controls:** #63 (Lu 2025).
6. **Evaluate full energy budget:** #64 (Sun 2026).
7. **Alternative easier-to-test physical soaring:** #65 (Reddy 2018) and already-indexed #31 (ArduSoar).

**Verification scope:** titles/DOIs are collated from the project's literature review and recent source checks; the 2015 Richardson and 2016 Sachs papers' publisher records were rechecked on 2026-10-18. Reading all full texts and reproducing results remains future work.

## Internal evidence and methodology

- [Senior analysis overview](../../reports/analysis/README.md)
- [Gold vs. Silver/Bronze](../../reports/analysis/gold-vs-silver-bronze.md)
- [Platinum / Best vs. Gold](../../reports/analysis/platinum-vs-gold.md)
- [Project archetypes](../../reports/analysis/project-archetypes.md)
- [Engineering and robotics patterns](../../reports/analysis/engineering-robotics-patterns.md)
- [CWSF 2027 design implications](../../reports/analysis/cwsf2027-design-implications.md)
- [Original candidate architectures](../../reports/analysis/cwsf2027-candidate-architectures.md)
- [Prior-art checkpoint](../../reports/analysis/prior-art-checkpoint.md)
