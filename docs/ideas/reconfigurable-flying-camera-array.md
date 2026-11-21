# Reconfigurable flying camera array

**Working concept:** A drone swarm that acts as one distributed camera / synthetic aperture.  
**Status:** Visually compelling aerospace/imaging candidate; substantial direct prior art.

## Core idea

Multiple aircraft capture images from different positions and computationally combine them so that foreground vegetation or other occluders are suppressed while hidden targets become easier to see.

The swarm is not simply several independent cameras. Its geometry becomes part of the imaging system.

## Scientific question candidates

A final project would need to narrow this to a specific unresolved question, for example:

- How should a small swarm arrange viewpoints when localization is imperfect?
- When does additional aperture width improve hidden-target detection enough to justify flight cost?
- How robust is synthetic-aperture occlusion removal to pose error?
- Can viewpoint selection be adapted to actual target-detection confidence rather than geometric visibility alone?

## Experimental path

1. Reproduce single-camera versus multi-view synthetic-aperture imagery in simulation or from a positioning rig.
2. Measure occlusion removal / detection as a function of:
   - viewpoint separation;
   - localization error;
   - number of views;
   - target depth;
   - occlusion density.
3. Compare with:
   - single image;
   - simple averaging;
   - fixed synthetic aperture;
   - adaptive viewpoint selection.
4. Validate on controlled physical scenes.
5. Only then implement on multiple flying platforms.

## Practical application

- wilderness search and rescue;
- wildfire hotspot sensing;
- wildlife/forest monitoring;
- inspection through partial occlusion.

## Novelty risk

This area has **very strong direct prior art**. JKU's Airborne Optical Sectioning group has published:

- SAR through foliage;
- person classification;
- tracking;
- synthetic-aperture drone swarm strategies;
- adaptive swarms;
- fixed-wing AOS;
- multispectral fusion;
- surface-temperature reconstruction;
- anomaly datasets.

Therefore, “use a drone swarm to see through vegetation” is already established. A 2027 project needs a sharply different question or validation regime.

## CWSF-analysis connection

This could fit the **measurement instrument** archetype very well if Chris treats the swarm as a scientific imaging instrument and characterizes its error/limits against an independent reference.

It becomes weaker if it is only a visual demo.

## References

1. **Schedl, Kurmi & Bimber (2020).** Search and rescue with airborne optical sectioning.  
   https://www.nature.com/articles/s42256-020-00261-3

2. **Schedl, Kurmi & Bimber (2021).** Autonomous Drones for Search and Rescue in Forests.  
   https://doi.org/10.1126/scirobotics.abg1188

3. **Kurmi et al. (2022).** Through-Foliage Tracking with Airborne Optical Sectioning.  
   https://spj.science.org/doi/10.34133/2022/9812765

4. **Nathan, Kurmi & Bimber (2023).** Drone swarm strategy for detection/tracking of occluded targets.  
   https://www.nature.com/articles/s44172-023-00104-0

5. **Nathan et al. (2025).** Autonomous drone swarm among dense vegetation.  
   https://www.nature.com/articles/s44172-025-00546-8

6. **Youssef & Bimber (2025).** DeepForest: sensing into self-occluding vegetation.  
   https://spj.science.org/doi/10.34133/remotesensing.0907

7. **Youssef et al. (2026).** Through-Foliage Surface-Temperature Reconstruction for Early Wildfire Detection.  
   https://www.nature.com/articles/s44488-026-00012-0

8. **Nathan et al. (2026).** Aerial color image anomaly dataset for search missions in complex forested terrain.  
   https://www.nature.com/articles/s41597-026-07101-w

9. **JKU AOS repository.** Code, simulation, datasets and swarm tools.  
   https://github.com/JKU-ICG/AOS
