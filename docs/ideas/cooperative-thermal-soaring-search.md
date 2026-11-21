# Cooperative thermal soaring for search

**Working concept:** Autonomous powered gliders exploit rising air while performing a search mission and optionally share useful atmospheric information.  
**Status:** Highly interesting aerospace extension; not preferred as the minimum project's critical path.

## Later refinement — Learning to Soar Together

[Learning to Soar Together: Performance-Aware Cooperative Search with Autonomous Gliders](learning-to-soar-together.md), documented 2026-09-21, develops the user's proposal to combine Flato et al.'s individual thermal-soaring research with SKYSURF. Its focus is the interaction between local flight capability and team decisions, with an A–E comparison that separates controller improvements, cooperation, straightforward integration, and the proposed performance-aware planner.

That separate note preserves the detailed research question, hypotheses, evaluation plan, physical validation stages, novelty boundaries, and checked references. It is a candidate for serious investigation; it does not retroactively change this broader concept's scope or the earlier recommendation.

## Aerospace appeal

This idea combines:

- fixed-wing aerodynamics;
- atmospheric structure;
- autonomous soaring;
- energy management;
- multi-aircraft coordination;
- search/surveillance.

The aircraft can convert atmospheric energy into altitude, then spend that altitude on useful mission flight.

## Scientific question candidates

Possible questions include:

> When should a search aircraft divert to rising air, and when should it ignore the opportunity because the search task is more urgent?

and:

> When does another aircraft's report of rising air improve that decision, and when does staleness make the detour harmful?

## Proposed hypothesis

Thermal exploitation can extend mission endurance, but maximum endurance does not necessarily maximize target-finding success before a deadline. Shared thermal reports may help only when the atmospheric feature persists long enough and the travel cost is low enough.

## Proposed experiment

Start with an established glider/soaring model and a simple search task.

Vary:

- thermal lifetime/strength;
- distance to thermal;
- target-search urgency;
- communication delay;
- energy state.

Compare:

- ignore thermals;
- individual thermal exploitation;
- shared thermal reports;
- mission-aware diversion rule.

Measure:

- target-finding success;
- mission time;
- electrical energy;
- altitude/endurance;
- wasted detours.

Later validate pieces physically using an established autopilot/soaring controller.

## Practical solution path

A future fleet of powered gliders could conduct persistent wide-area reconnaissance while opportunistically using atmospheric lift.

The project should show that extra endurance **improves the mission**, not merely that the aircraft can stay aloft longer.

## Major prior-art overlap

Autonomous thermalling itself is established, including real UAV experiments. A 2024 Nature Communications paper studies learning principles for thermal soaring. A February 2026 preprint, SKYSURF, directly studies cooperative powered gliders that exploit thermals while monitoring targets.

**Publication update checked 2026-09-21:** SKYSURF also has a journal version published on 20 August 2026 in the *International Journal of Intelligent Robotics and Applications*. The journal record is linked in reference 4; detailed assumption discussions in the newer concept note remain explicitly tied to arXiv v1 rather than an unreviewed subscription full text.

Therefore, none of these is a novelty claim:

- autonomous thermalling;
- glider endurance extension;
- sharing thermal information;
- cooperative powered glider monitoring.

The research question must be narrower and materially different.

## CWSF-analysis connection

This is a strong **engineering experiment** candidate if the project isolates a measurable relationship between atmospheric opportunity, mission urgency and useful task performance.

It becomes risky if too much depends simultaneously on aircraft reliability, thermal weather, multi-aircraft flight and a new planner.

## References

1. **Tabor, Guilliard & Kolobov (2018).** *ArduSoar: an Open-Source Thermalling Controller for Resource-Constrained Autopilots.*  
   https://arxiv.org/abs/1802.08215

2. **ArduPilot Plane — Soaring documentation.**  
   https://ardupilot.org/plane/docs/soaring.html

3. **Flato et al. (2024).** *Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* Nature Communications.  
   https://doi.org/10.1038/s41467-024-48670-x

4. **Mohamadi & Kara (2026).** *SKYSURF: A Self-learning Framework for Persistent Surveillance using Cooperative Aerial Gliders.*  
   https://arxiv.org/abs/2602.12838  
   Full text: https://arxiv.org/html/2602.12838v1  
   Journal record (published 20 August 2026): https://doi.org/10.1007/s41315-026-00553-8

5. **Fixed-wing concept note:** [Flying Farther Is Not Enough](fixed-wing-autonomous-search.md)

6. **Focused two-paper refinement:** [Learning to Soar Together](learning-to-soar-together.md)
