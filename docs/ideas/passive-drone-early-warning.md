# Passive drone early warning: reliable acoustic and optical sensing

**Documented:** 2026-10-18  
**Status:** Unselected candidate. No operational detector or disabling/interception technology is proposed.  
**Origin:** The user proposed "technologies to identify and disable FPV" from a civilian-protection perspective after [watching a documentary](https://www.youtube.com/watch?v=CyA9s4MEwnw). This note deliberately focuses on **passive early warning**, not neutralization.

[Idea library](README.md) · [Airborne camera detection](humanitarian-fixed-wing-drone-detection.md) · [Integrated proposal](search-for-safety-humanitarian-aerial-intelligence.md)

## 1. Problem and scope

A humanitarian warning system needs to be reliable under wind, machinery, bird activity, camera clutter, lighting variation and sensor dropout. Audio and cameras can fail differently, but combining them can also add complexity or count weak evidence twice. An alert that "a small airborne object may be present" is **not** proof of hostility.

The research uses benign nonweaponized drones, permitted recordings and non-operational offline experiments. **Jamming, spoofing, interception, capture, hacking, kinetic defenses, live tracking, and weaponization are excluded.**

## 2. Scientific question

> Does calibrated fusion of passive optical and acoustic evidence produce more reliable early warnings than a well-tuned single sensor at a fixed false-alarm/latency budget, and when does additional sensing fail to help?

More specifically, can an explicit uncertain/abstain state prevent false reassurance during sensor failure or unfamiliar acoustic/visual environments?

### Falsifiable hypotheses

- **H1:** Complementary optical and acoustic evidence improves recall at a fixed false-alarm rate in some controlled conditions.
- **H2:** In noise and domain shift, naive fusion may worsen reliability, while a calibrated rule makes uncertainty more apparent.
- **H3:** The best method may depend on the environment; under benign clear conditions, a single sensor may outperform or match fusion.

These are proposed predictions, not results.

## 3. Experimental plan

**Stage A — data and ground truth:** Obtain labelled benign drone-present and drone-absent recordings under lawful, supervised conditions. Record environmental conditions and synchronization. Include background wind, vehicles, birds and machinery without involving unsuspecting people. Avoid collecting private communications.

**Stage B — separate channel baselines:** Audio-only classifier, visual-only classifier and fixed thresholds. Measure precision/recall, false alarms per independent recording hour, latency and calibration. Do not treat adjacent audio chunks or video frames as independent samples.

**Stage C — fusion:** Compare AND/OR rules, simple probability fusion and a calibrated uncertainty-aware fusion/abstain method under the *same* recordings, tuning budget and processing limit. Ablate the confidence calibration and sensor-dropout handling to isolate their contribution.

**Stage D — robustness:** Hold out entire recording sessions and environments. Test missing audio/visual input, wind noise, visual obstruction and negative examples. Present performance curves rather than a single flattering accuracy score.

| Type | Candidate variables |
|---|---|
| Independent | Sensor modality, noise, visibility, sensor availability, fusion/abstention strategy |
| Dependent | False positives per hour, recall, latency, risk–coverage curve, calibration |
| Controls | Same sessions, labels, thresholds-selection rules, signal-processing budget |
| Replication | Independent recording sessions/environments |

**Success:** Reproducible reliability gains at predeclared false-alarm and latency constraints. **Failure:** A tuned single-sensor baseline does just as well. **Inconclusive:** False-positive samples or independently labelled sessions are insufficient, or no credible acoustic/fusion baseline is reproduced.

## 4. Prior art and novelty gate

Visual UAV monitoring is already well established; Anti-UAV and Drone-vs-Bird provide relevant comparison material. Acoustic and multimodal drone detection are also known approaches, but **a focused peer-reviewed acoustic/fusion closest-work matrix has not yet been completed**. The novel contribution, if any, must be a tested reliability/uncertainty principle rather than "a microphone can hear drones" or "two sensors are better."

Do not assume a microphone on a powered survey aircraft will work: propulsion noise may dominate. Stationary passive sensing can be tested independently of the fixed-wing idea.

## 5. Law, privacy and ethics

No radio interception, signal disruption, or RF countermeasure experiments. Canada's ISED says RF counter-drone interference/spoofing systems are jammers and are generally prohibited; passive RF scanners can also raise receiver compliance/licensing requirements. Do not infer anyone's identity or intent from a detection. Protect recordings, obtain consent and follow current Transport Canada rules for drone demonstrations.

The immediate scientific goal is **honest civilian warning reliability**, not tactical effectiveness or operational conflict deployment.

## 6. Next gates

1. Identify permitted drone-positive and drone-negative recordings.
2. Reproduce audio-only and camera-only baselines, with session-level splits.
3. Complete recent acoustic/visual fusion prior-art review.
4. Predeclare false-alarm, latency and abstention evaluation.
5. Continue only if a distinct result survives unseen conditions.

## References (background verified at institutional/abstract level)

- User documentary: https://www.youtube.com/watch?v=CyA9s4MEwnw
- UN HRMMU, *Deadly drones*, June 2025: https://ukraine.ohchr.org/en/Deadly-drones-Civilians-at-risk-from-short-range-drones-in-frontline-areas-of-Ukraine-24-February-2022-30-April-2025
- Isaac-Medina et al. (2021), visual UAV detection benchmark: https://openaccess.thecvf.com/content/ICCV2021W/AntiUAV/html/Isaac-Medina_Unmanned_Aerial_Vehicle_Visual_Detection_and_Tracking_Using_Deep_Neural_ICCVW_2021_paper.html
- Drone-vs-Bird: https://github.com/wosdetc/challenge
- ISED, jamming prohibition: https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/safety-and-compliance/compliance-and-enforcement/jammers-are-prohibited-canada-thats-law
- ISED, RF scanner receiver guidance: https://ised-isde.canada.ca/site/certification-engineering-bureau/en/notice-2024-drs0010
