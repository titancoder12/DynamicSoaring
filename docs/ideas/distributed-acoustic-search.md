# Distributed acoustic search with flying robots

**Working concept:** A flying team that searches by listening as well as looking.  
**Status:** Interesting alternative; experimentally difficult.

## Practical problem

Visual search fails under foliage, darkness, terrain occlusion or poor contrast. A person may also produce acoustic cues such as shouting, whistles or alarms.

However, aircraft carrying microphones generate their own strong aerodynamic and rotor/propeller noise.

That creates a useful physical tension:

> The vehicle that carries the sensor also contaminates the measurement.

## Scientific question candidates

A focused project might ask:

> Can coordinated aircraft positions and listening schedules improve distress-sound detection under self-noise compared with continuous onboard listening?

or:

> When does spatial cooperation between multiple noisy airborne microphones outperform a single aircraft at the same total sensing time?

## Proposed experiment

Use controlled prerecorded signals—not real emergency subjects.

Vary:

- source strength;
- aircraft distance;
- background noise;
- propulsion state;
- listening position;
- number of aircraft;
- synchronization strategy.

Compare:

- continuous listening;
- motor-idle/glide listening windows where safe and platform-appropriate;
- single aircraft;
- multiple aircraft;
- fixed beamforming/localization baseline;
- proposed cooperative strategy.

Measure:

- detection rate;
- false alarms;
- localization error;
- time/resource cost.

## Practical solution path

A final system could fuse acoustic cues with aerial visual search, using sound only when it adds information.

Fixed-wing gliders could be interesting because gliding/low-power periods may reduce self-noise, but that hypothesis must be measured.

## Novelty risk

Aerial acoustic sensing and source localization already have prior art. The specific gap would need a dedicated literature review.

The project is also experimentally harder than camera-based search because synchronization, wind noise, propulsion noise and acoustic reflections can dominate the result.

## CWSF-analysis connection

This fits the **measurement instrument** and **engineering experiment** archetypes particularly well:

- characterize sensor contamination;
- identify operating regimes;
- redesign sensing behaviour;
- demonstrate whether the redesign improves the real task.

## References

1. **DroneAudioset (2025).** Drone-recorded search-and-rescue audio dataset / NeurIPS 2025 Datasets and Benchmarks work.  
   https://arxiv.org/abs/2510.15383

2. **Transport Canada.** Flight rules and operating guidance for any physical trials.  
   https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone

3. Internal CWSF design framework: [Project archetypes](../../reports/analysis/project-archetypes.md) and [Engineering patterns](../../reports/analysis/engineering-robotics-patterns.md).
