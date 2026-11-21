# Humanitarian small-drone observation from a fixed-wing surveillance aircraft

**Documented:** 2026-10-18  
**Status:** Unselected CWSF 2027 candidate; proposed experiments, not results, a flight plan, operational detection, or verified novelty.  
**Origin:** The user's idea of detecting FPV-sized drones from a fixed-wing survey aircraft, prompted by [this documentary](https://www.youtube.com/watch?v=CyA9s4MEwnw). The video's full transcript was not independently checked; this note is an original idea proposal, not an account of specific scenes.

[Idea library](README.md) · [Passive early warning](passive-drone-early-warning.md) · [Integrated humanitarian concept](search-for-safety-humanitarian-aerial-intelligence.md) · [Fixed-wing search](fixed-wing-autonomous-search.md)

## 1. Humanitarian problem and research objective

Detecting a tiny airborne object can be difficult against trees, clouds, birds, motion blur and shifting camera perspectives. An aircraft-mounted camera adds platform motion. False alarms can erode trust; missed objects and overconfident negative assessments can create false reassurance. Detecting an aircraft does **not** determine its intent, operator or whether it poses a threat.

**Research question:** Under changes in camera movement, apparent object size and background clutter, when does a visual detector become confidently wrong, and can an uncertainty-aware warning or abstention rule improve reliability under the same resource limits?

## 2. Falsifiable hypotheses

- **H1:** Performance and confidence calibration deteriorate when a detector trained on stable-view footage faces new moving-camera conditions.
- **H2:** A calibrated selective/abstaining rule reduces overconfident misses or wrong alarms at the cost of fewer definitive alerts.
- **H3:** Multiple video frames may produce less new evidence than expected if observation errors are strongly correlated; genuinely different views may help under some conditions.

None is an established result. A finding that ordinary well-tuned detection works as well is meaningful.

## 3. Proposed experimental program

**Stage A — Benchmark and data audit:** Find lawfully usable, labelled benign drone/bird footage. Record camera origin, environment, session, target-present and target-absent labels. Hold out entire recording sessions/environments; do not randomly split highly correlated adjacent video frames. Do not claim a dataset is moving-camera if that has not been verified.

**Stage B — Reproduce a simple detector:** Compare an established visible-image detector with a straightforward temporal consistency baseline on identical video. Evaluate both positive and negative footage and hard negatives such as birds.

**Stage C — Test reliable uncertainty:** Evaluate confidence calibration, an abstention/need-more-evidence option and (optionally) a method that discounts repeated correlated observations. Keep detector model and underlying footage fixed while isolating the effect of the confidence rule.

**Stage D — Physical check only if warranted:** Consider stationary and safely moving camera footage of a benign, nonweaponized hobby drone in a permitted, supervised test setting. Fixed-wing *air-to-air* filming is not required for the first experiment and needs separate legal/safety planning if ever undertaken.

### Candidate variables and endpoints

| Kind | Proposed items |
|---|---|
| Independent | Background, apparent drone size, camera motion, visibility, fusion rule and abstention policy |
| Dependent | Recall, precision, false alarms per recording hour, latency, calibration error and risk–coverage tradeoff |
| Controls | Same labelled sessions, model-selection budget, threshold tuning protocol, compute limit and evaluation splits |
| Independent replicate | A recording session or scenario, not each video frame |

**Primary proposed endpoint:** reliability at a fixed false-alarm and latency budget on held-out sessions. Display performance as a risk–coverage curve so that making no predictions is not mistakenly called success.

**Comparators/ablations:** (1) single-frame detector, (2) temporal smoothing, (3) calibrated warning threshold, (4) proposed independence-aware/abstaining method, (5) the proposed method with its independence adjustment removed, if implemented. Use fair resource accounting.

**Success:** A reproducible, bounded improvement in reliability in a specified hard regime, with intervals across independent sessions. **Failure:** No advantage versus a strong basic method. **Inconclusive:** Inadequate negative examples, poorly labelled data, data leakage, or no true moving-camera holdout.

## 4. Prior art, novelty and ethics

UAV visual detection/tracking and benchmarks are established. Anti-UAV and Drone-vs-Bird directly address tracking and confusion with small moving objects. Simply training a neural network to detect drones or recording imagery from another drone is *not* an original contribution. A closest-work matrix must check small-object errors, camera motion, probability calibration, temporal dependence, dataset shift, error costs and available code.

This is a **passive observation study** using benign data. No identifying or targeting persons, hostile-intent inference, real-time combat tracking, publication of live locations, jamming or interception. Obtain permissions for recordings and data. Any actual flying must follow applicable Transport Canada requirements and site restrictions.

## 5. CWSF connection and decision gates

Builds on [false confidence](false-confidence-under-model-mismatch.md), [occluded observation](cooperative-aerial-search-under-occlusion.md), and [fixed-wing search](fixed-wing-autonomous-search.md). The science should yield a *failure boundary or confidence principle*, not just a flying demonstration.

1. Audit a suitable moving/static-camera dataset and lawful reuse terms.
2. Reproduce a credible detection baseline and measure hard-negative errors.
3. Check the closest 2024–2026 work on small-drone detection reliability and calibrated abstention.
4. Freeze held-out evaluation and investigate a narrow hypothesis.
5. Continue only if meaningful research remains without needing a multi-UAV hardware build.

## References (abstract/institutional-page check only; not exhaustive)

- User documentary: https://www.youtube.com/watch?v=CyA9s4MEwnw (inspiration; full video not verified).
- UN HRMMU, *Deadly Drones*, June 2025: https://ukraine.ohchr.org/en/Deadly-drones-Civilians-at-risk-from-short-range-drones-in-frontline-areas-of-Ukraine-24-February-2022-30-April-2025
- Isaac-Medina et al. (2021), UAV visual detection/tracking benchmark: https://openaccess.thecvf.com/content/ICCV2021W/AntiUAV/html/Isaac-Medina_Unmanned_Aerial_Vehicle_Visual_Detection_and_Tracking_Using_Deep_Neural_ICCVW_2021_paper.html
- Jiang et al. (2021), Anti-UAV multimodal benchmark: https://arxiv.org/abs/2101.08466
- Drone-vs-Bird challenge: https://github.com/wosdetc/challenge
- Transport Canada, drone rules: https://tc.canada.ca/en/aviation/drone-safety/learn-rules-you-fly-your-drone
