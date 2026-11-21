# Cooperative aerial search under occlusion

**Working title:** *Search Without False Confidence — Cooperative Aerial Search Under Occlusion*  
**Status:** Current leading practical-aerospace candidate for investigation.

## Practical problem

A drone can fly over the correct location without obtaining a view that allows a partially hidden target to be detected. Multiple nearby views may share the same blind spot, so repeated negative observations do not necessarily provide independent evidence that an area is clear.

## Scientific question

> Under partially occluded conditions, can a flying team that accounts for viewpoint quality and correlated missed detections reduce false “searched-area” decisions and improve target finding compared with credible search methods at the same total flight budget?

This is deliberately stronger than “do different angles help?”

## Proposed hypothesis

Selective verification from complementary viewpoints will improve target-finding reliability when earlier observations share common blind spots, but will provide little value or waste resources in open/easy environments.

## Proposed contribution

A possible contribution is a lightweight cooperative verification rule that:

1. identifies when several negative observations are not sufficiently independent;
2. chooses a meaningfully different verification view;
3. trades verification cost against exploration of new territory;
4. remains useful when the system's visibility or detection model is imperfect.

This is a candidate gap, not yet verified novelty.

## Proposed experimental programme

### Stage 1 — measure the sensing relationship

Use one camera and controlled obstructed scenes with known target locations.

Measure how:

- occlusion;
- camera position;
- viewpoint diversity;
- detection reliability

affect the probability of detecting a target.

The first scientific task is to determine whether repeated views actually fail together under the available sensing setup.

### Stage 2 — compare search policies

Use measured observations in a search simulator.

Compare:

- lawnmower/uniform search;
- visibility-aware search;
- correlation-aware perception;
- equally costly random revisits;
- proposed targeted verification;
- independent vs cooperative agents.

Keep the detector, fleet size and total flight/measurement resources matched.

### Stage 3 — close the loop with real aircraft

Use a small aerial team and benign dummy targets in controlled scenes. Demonstrate that the team chooses useful new viewpoints rather than simply collecting more frames.

## Outcomes

Possible primary outcomes:

- target-finding success at fixed resources;
- false searched-area decisions;
- time to valid detection.

Secondary outcomes:

- false alarms;
- area resolved/searchable;
- travel cost;
- number of verification views.

Target-absent trials are necessary so an excessively cautious system cannot appear perfect simply by refusing to clear any area.

## Why this fits the CWSF analysis

This combines three evidence-grounded archetypes:

- benchmark/failure analysis;
- mechanism-informed redesign;
- integrated functional system.

It creates a complete chain:

```text
real sensing failure
   ↓
measured explanation
   ↓
new decision rule
   ↓
controlled comparison
   ↓
physical aerial implementation
   ↓
practical search result
```

## Novelty risks

Several relevant ideas already exist:

- correlated observation models in active perception;
- airborne optical sectioning;
- occlusion-aware next-best-view planning;
- autonomous multi-drone search;
- adaptive drone-swarm synthetic aperture imaging.

Therefore, none of the following is a valid novelty claim by itself:

- multiple drones search for a person;
- different viewpoints help;
- observations can be correlated;
- a swarm adapts its formation;
- a drone chooses a next best view.

The final contribution must be narrower.

## References

1. **Velez et al. (2012).** Active perception planning with correlations between object detections from nearby viewpoints. JAIR.  
   https://jair.org/index.php/jair/article/view/10770

2. **Schedl, Kurmi & Bimber (2020).** *Search and rescue with airborne optical sectioning.* Nature Machine Intelligence.  
   https://www.nature.com/articles/s42256-020-00261-3

3. **Schedl, Kurmi & Bimber (2021).** *Autonomous Drones for Search and Rescue in Forests.* Science Robotics.  
   https://doi.org/10.1126/scirobotics.abg1188

4. **Nathan, Kurmi & Bimber (2023).** *Drone swarm strategy for the detection and tracking of occluded targets in complex environments.* Nature Communications Engineering.  
   https://www.nature.com/articles/s44172-023-00104-0

5. **Nathan et al. (2025).** *An Autonomous Drone Swarm for Detecting and Tracking Anomalies among Dense Vegetation.* Nature Communications Engineering.  
   https://www.nature.com/articles/s44172-025-00546-8

6. **Next Best View planning for occluded UAV search (2025 preprint).**  
   https://arxiv.org/html/2511.18353v1

7. **ForestPersons dataset / paper (2026).** Missing-person detection in forested environments.  
   https://arxiv.org/html/2603.02541v1  
   Dataset: https://huggingface.co/datasets/etri/ForestPersons

8. **JKU Airborne Optical Sectioning research/code repository.**  
   https://github.com/JKU-ICG/AOS

9. **Crazyswarm2.** Open-source multi-quadrotor research platform.  
   https://imrclab.github.io/crazyswarm2/

10. **Transport Canada.** Drone safety / operating rules.  
    https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone
