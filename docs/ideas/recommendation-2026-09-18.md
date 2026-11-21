# Current CWSF 2027 recommendation and selection reasoning

**Date:** 2026-09-18  
**Scope:** Chris's current interests: aerospace, swarms of flying machines, and possible search-and-rescue applications.  
**Status:** Strategy recommendation for the next investigation stage; **not** a prediction of a CWSF medal and **not** a final topic selection.

## Executive recommendation

The current order for **which ideas to investigate most seriously next** is:

1. **Cooperative aerial search under occlusion — “Search Without False Confidence”**
2. **Energy- and detection-aware fixed-wing autonomous search — “Flying Farther Is Not Enough”**
3. **Recalibration versus exploration**
4. **Cooperative thermal soaring for search**
5. **Delayed communication tradeoff**

The broader information-foraging observatory, balloon profiling, flying-camera-array, rare-event, model-discrimination, heterogeneous-sensor and acoustic ideas remain useful alternatives or supporting research modules.

This ordering reflects the present combination of:

- scientific question clarity;
- practical usefulness;
- fit with Chris's interests;
- ability to produce a controlled experiment;
- ability to generate useful knowledge from a negative result;
- plausible student-scale physical validation;
- known prior-art overlap;
- integration risk.

It does **not** estimate award probability.

## What the historical analysis actually supports

The repository review does not identify a universal trait that separates Gold from Silver/Bronze. Strong baselines, physical testing, AI, controls and failure analysis occur across medal levels.

The most transferable design lesson is:

> **Make the question, comparison, evidence and claim fit together.**

The project-archetype analysis identifies recurring structures such as:

- measurement instrument;
- scientific inference system;
- engineering experiment;
- benchmark/failure analysis;
- integrated functional system;
- mechanism-informed redesign.

For Chris's interests, the most attractive combination is:

> **measurement + inference + controlled engineering evaluation + practical implementation**

This is a design preference based on the reviewed cases, not a discovered judging rule.

## 1 — Cooperative aerial search under occlusion

**Document:** [cooperative-aerial-search-under-occlusion.md](cooperative-aerial-search-under-occlusion.md)

### Why it leads

This idea creates a particularly coherent science-to-solution chain:

```text
real SAR sensing limitation
      ↓
measure how repeated views fail
      ↓
explain when multiple observations are redundant
      ↓
develop a verification / viewpoint rule
      ↓
compare with credible existing methods
      ↓
implement on a small flying team
      ↓
measure target-finding reliability
```

It directly uses the flying swarm for a meaningful reason: changing the aircraft positions changes what can actually be observed.

It also allows the central scientific mechanism to be tested with one camera and controlled scenes **before** the entire fleet is operational. That protects the project from hardware delays while keeping real aerial implementation as an intended final milestone.

### What could make it strong

A bounded contribution such as:

> A lightweight verification method that detects when apparently repeated negative observations share the same blind spot and selects a genuinely informative additional viewpoint under a fixed search budget.

The result could be positive or negative. For example, Chris might identify a regime where additional viewpoints stop adding independent evidence.

### Main risk

Prior art is substantial:

- correlated object detections from nearby viewpoints;
- next-best-view planning;
- airborne optical sectioning;
- autonomous drone SAR;
- adaptive multi-drone occlusion removal.

Therefore, “different views help,” “observations are correlated,” and “a swarm searches through vegetation” are **not** novelty claims. The first task must be a focused closest-work matrix.

### Current decision gate

Retain as #1 only if a narrow failure/verification question survives comparison with the strongest correlation-aware and visibility-aware methods.

## 2 — Energy- and detection-aware fixed-wing autonomous search

**Document:** [fixed-wing-autonomous-search.md](fixed-wing-autonomous-search.md)

### Why it is a close second

This is the strongest direct match to Chris's interest in **aeroplanes**. Flight physics is part of the research rather than merely the transportation platform.

The strongest current framing is:

> How do flight decisions affect both electrical energy and useful target observations, and can a planner using the measured relationship improve search success before a deadline?

This creates a compelling chain:

```text
aerodynamic / flight choice
      ↓
measured energy + observation quality
      ↓
established tradeoff
      ↓
autonomous decision rule
      ↓
real fixed-wing implementation
      ↓
target-finding comparison
```

### Why it is not #1 yet

The concept currently has more feasibility unknowns:

- aircraft;
- instrumentation;
- test field;
- repeatable autonomous flight;
- flight permissions/supervision;
- camera performance;
- battery/airspeed measurement.

It also needs a stronger prior-art review of energy-aware aerial search and sensor-aware path planning. A simple speed/altitude optimization would not be enough.

### When it should become #1

Move this idea ahead of cooperative multirotor search if:

1. Chris is substantially more motivated by aeroplanes;
2. repeated instrumented fixed-wing flights are realistically available;
3. the literature review identifies a meaningful unresolved energy-versus-search question;
4. the first measurements show a nontrivial tradeoff rather than a trivial optimum.

Motivation and execution quality matter. A deeply tested project Chris genuinely wants to build is preferable to a theoretically stronger idea that never reaches rigorous physical validation.

## 3 — Recalibration versus exploration

**Document:** [recalibration-versus-exploration.md](recalibration-versus-exploration.md)

### Why retain it

This has one of the cleanest physical experiments:

- real sensors;
- independent reference;
- controlled drift;
- measurable map error;
- clear resource tradeoff.

It matches the historical **measurement instrument** archetype extremely well.

### Why it is behind the aerospace search ideas

It is less directly connected to Chris's strongest interests. It is a very good fallback if aircraft logistics threaten project depth.

It can also become a subsystem of an aerial project later.

### Main risk

Adaptive/uncertainty-driven calibration already exists. The project needs a distinct calibration-versus-coverage result rather than merely a new trigger.

## 4 — Cooperative thermal soaring for search

**Document:** [cooperative-thermal-soaring-search.md](cooperative-thermal-soaring-search.md)

### Why it is exciting

This is arguably the most compelling **pure aerospace vision**:

- fixed-wing aerodynamics;
- atmospheric energy;
- autonomous soaring;
- multi-aircraft cooperation;
- persistent search.

### Why it is not the preferred main commitment

It has both high prior-art overlap and high experimental dependence.

Existing work already covers:

- autonomous thermalling;
- real small-UAV thermalling;
- learning-based thermal soaring;
- cooperative powered gliders using thermals for monitoring.

A successful project would also depend on flight reliability, atmospheric conditions, soaring estimation and mission planning simultaneously.

### Recommended role

Treat thermal soaring as an **extension** of the fixed-wing search project unless a sharper, clearly unresolved question emerges.

## 5 — Delayed communication tradeoff

**Document:** [delayed-communication-tradeoff.md](delayed-communication-tradeoff.md)

### Why retain it

It is intellectually continuous with Chris's previous swarm work and has excellent opportunities for:

- communication ablation;
- matched resource accounting;
- regime maps;
- negative results.

### Why it falls behind

Very recent research directly addresses:

- stale decentralized beliefs;
- conservative fusion;
- adaptive communication/rendezvous windows.

A generic “when is communication useful?” project is therefore too close to current work.

The idea becomes stronger only when communication is embedded in a **specific physical sensing problem** where it changes a meaningful inference.

## Other idea dispositions

### Information-foraging airborne observatory

[Document](information-foraging-airborne-observatory.md)

Retain as the **umbrella intellectual direction**, not the novelty claim. It helps connect the individual projects conceptually.

### False confidence under model mismatch

[Document](false-confidence-under-model-mismatch.md)

Strong research mechanism and originally the Work analysis's first low-hardware choice. The cooperative aerial-search idea is effectively a search-and-rescue-specific, physical refinement of this theme.

### Adaptive atmospheric balloon profiling

[Document](adaptive-atmospheric-profiling-balloons.md)

Retain for future atmospheric-science work. Current concern is validation/logistics and a weaker direct fit to the immediate SAR interest.

### Mapping versus rare-event detection

[Document](mapping-versus-rare-event-detection.md)

Useful research module. Could become central if Chris focuses on wildfire, distress-target detection or intermittent environmental anomalies.

### Physical-model-discrimination sampling

[Document](model-discrimination-sampling.md)

Scientifically strong reserve. It offers deeper physical inference but currently has a weaker connection to the desired practical flying-search system.

### Heterogeneous sensor assignment

[Document](heterogeneous-sensor-assignment.md)

Useful extension after a core sensing problem is solved. Avoid adding sensor-allocation complexity too early.

### Reconfigurable flying camera array

[Document](reconfigurable-flying-camera-array.md)

Extremely relevant and visually compelling, but direct prior art in Airborne Optical Sectioning is unusually strong. Better treated as a baseline/inspiration unless a distinct constraint or imaging problem is identified.

### Distributed acoustic search

[Document](distributed-acoustic-search.md)

Interesting alternative because aircraft self-noise creates a real measurement problem. Experimental synchronization/noise challenges and unresolved prior-art depth currently make it a secondary candidate.

## Why this recommendation is not a medal forecast

The Senior historical dataset is observational and incomplete. The analysis explicitly found:

- useful baselines across Gold/Silver/Bronze;
- physical testing across medal levels;
- sophisticated AI across medal levels;
- meaningful failure analysis outside Gold;
- no fully balanced medal-matched cohort.

The Platinum/Best audit also did not establish a universal top-award signature.

Accordingly, this recommendation answers:

> **Which project direction currently offers the strongest combination of scientific depth, practical solution, Chris-fit and feasible validation?**

It does **not** answer:

> Which topic is guaranteed or statistically most likely to win a medal?

## Immediate next research step

Run a focused **two-candidate feasibility and novelty sprint**:

### Candidate 1
Cooperative aerial search under occlusion.

Produce a closest-work matrix covering at minimum:

- Velez et al. correlation-aware active perception;
- airborne optical sectioning;
- autonomous forest SAR;
- 2023/2025 swarm occlusion work;
- recent next-best-view planning.

Then perform a one-camera controlled occlusion pilot.

### Candidate 2
Energy- and detection-aware fixed-wing search.

Produce a closest-work matrix covering:

- energy-aware aerial search;
- sensor-aware flight planning;
- fixed-wing autonomous survey;
- ArduSoar/autonomous thermalling;
- SKYSURF/cooperative gliders.

Then measure whether flight speed/altitude create a repeatable, nontrivial energy-versus-detection tradeoff using the intended camera/airframe or a representative test setup.

## Selection criterion after the sprint

Choose the idea for which Chris can answer all four:

1. **What exact limitation remains after the best existing method?**
2. **What experiment could prove our proposed explanation wrong?**
3. **What practical system directly uses the resulting knowledge?**
4. **Can we execute enough independent physical validation before CWSF 2027?**

If both survive, Chris's intrinsic preference should be a major factor. The goal is not merely the most sophisticated concept; it is the deepest project he can actually complete, understand and defend.
