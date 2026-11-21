# 06 — Papers, Prior Art and Engineering References

**Source review date:** 2026-10-18. **Source boundary:** summaries below are derived from publisher-accessible abstracts/landing pages and technical documentation unless otherwise noted. Full-paper reproductions require reading methods, figures and supplementary material before assuming parameter values or software availability.

[Project home](README.md) · [Physics](02-physics-and-modeling.md)

## A. Four principal papers explicitly discussed

### [R1] Kim et al. (2019) — neural-feedback dynamic soaring

**Kim, Seong-hun; Lee, Jihoon; Jung, Seungyun; Lee, Hanna; Kim, Youdan.**  
*Deep Neural Network-Based Feedback Control for Dynamic Soaring of Unpowered Aircraft.* IFAC-PapersOnLine 52(12), 117–121 (2019).  
DOI: https://doi.org/10.1016/j.ifacol.2019.11.079  
Publisher: https://www.sciencedirect.com/science/article/pii/S2405896319310158  
Author publication list: https://jihoonlee91.github.io/publications.html

**What it establishes:** A neural-network feedback law was trained from optimized state/control trajectory pairs, then numerically demonstrated on several wind profiles. It directly combines neural control with albatross-type shear harvesting.

**Use in this project:** Study the physics assumptions, reproduce a feedback baseline, and distinguish neural imitation of an optimizer from reinforcement learning trained by interacting with a simulator. It is a reference to learn from, not evidence that our aircraft will succeed.

### [R2] Zou et al. (2025) — PPO-based trajectory optimization

**Zou, Wanyong; Li, Ni; An, Fengcheng; Wang, Kaibo; Dong, Changyin.**  
*A novel trajectories optimizing method for dynamic soaring based on deep reinforcement learning.* Defence Technology 46, 99–108 (2025).  
DOI: https://doi.org/10.1016/j.dt.2024.12.007  
Publisher: https://www.sciencedirect.com/science/article/pii/S2214914724002812

**What it establishes:** Dynamic-soaring trajectories parameterized with Fourier functions were optimized via PPO-based RL and compared with a nonlinear programming approach. The published abstract reports a smoother trajectory and improvements in maximum thrust and airspeed variations in the authors' setup.

**Use in this project:** A practical source for flight dynamics, trajectory parameterization, baseline comparisons, and learning approach. Do not assume its percentage improvements predict reduced battery energy or translate to FW-01.

### [R3] Lu, Xie & Ji (2025) — human-in-the-loop RL for planning plus control

**Lu, Yufeng; Xie, Fangfang; Ji, Tingwei.**  
*Human-in-the-loop reinforcement learning for dynamic soaring: A trajectory planning and control integrated system.* Engineering Applications of Artificial Intelligence 157, 111219 (2025).  
DOI: https://doi.org/10.1016/j.engappai.2025.111219  
Publisher: https://www.sciencedirect.com/science/article/abs/pii/S0952197625012205

**What it establishes:** Its authors combine optimal-trajectory generation, deep RL and a lower-level controller in a high-fidelity environment, and report autonomous simulated dynamic-soaring execution and limited robustness checks for wind disturbance and initial-state deviations. The *human-in-the-loop* phrase refers to researchers injecting expertise into learning design; it is not the same as requiring human piloting in every run.

**Use in this project:** Architectural precedent for separating flight planning from low-level stabilization, designing rewards/constraints, and evaluating robustness. Study its exact experimental access and limitations in full text before treating it as a faithful hardware guide.

### [R4] Sun et al. (2026) — full-mission energy management

**Sun, Sanya; Shao, Zhuang; Xu, Xiaoping; Zhou, Zhou.**  
*Enhancing UAV endurance: coupled optimization of dynamic soaring trajectory and high-fidelity powertrain energy management.* Applied Energy 416, 127955 (2026).  
DOI: https://doi.org/10.1016/j.apenergy.2026.127955  
Publisher: https://www.sciencedirect.com/science/article/pii/S0306261926006070

**What it establishes:** A coupled battery–ESC–motor–propeller model with trajectory/transition planning for a conventional fixed-wing UAV. The authors report a 23.1% total mission energy reduction compared with their straight-line cruise reference in their studied scenario, alongside other model-level and segment-level results.

**Use in this project:** Caution against measuring energy only as altitude change or control effort. Investigate battery power integration, transition penalties and whether short soaring loops actually help a full route mission. The paper's numbers are *published results in a specific setup*, not estimates for our aircraft.

## B. Additional foundational/adjacent publications

### [R5] Sachs (2005) — minimum shear strength

**Sachs, Gottfried.**  
*Minimum shear wind strength required for dynamic soaring of albatrosses.* Ibis 147(1), 1–10 (2005).  
DOI: https://doi.org/10.1111/j.1474-919x.2004.00295.x

**Why:** Foundational theory of wind-shear threshold and mechanism; useful when defining a measurable wind/airframe feasibility map.

### [R6] Deittert et al. (2009) — unpowered UAV dynamics

**Deittert, M.; Richards, A.; Toomer, C. A.; Pipe, A.**  
*Engineless Unmanned Aerial Vehicle Propulsion by Dynamic Soaring.* Journal of Guidance, Control, and Dynamics 32(5), 1446–1457 (2009).  
DOI: https://doi.org/10.2514/1.43270

**Why:** Classical dynamic-soaring trajectory/control modeling baseline. Read full paper for its precise assumptions.

### [R7] Flato et al. (2024) — RL for thermal soaring, NOT dynamic soaring

**Flato, Yoav; Harel, Roi; Tamar, Aviv; Nathan, Ran; Beatus, Tsevi.**  
*Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* Nature Communications 15, 4942 (2024).  
DOI: https://doi.org/10.1038/s41467-024-48670-x  
Open article: https://www.nature.com/articles/s41467-024-48670-x

**Why:** Valuable student-accessible example for RL training curriculum, sensor input, robustness and bird-inspired comparison. **Not evidence of dynamic soaring through vertical horizontal-wind shear**: this paper addresses rising thermals, and its bird inspiration is vulture flight. Relevant as a learning technique, not identical physics.

### [R8] Reddy et al. (2018) — RL thermal soaring in field

**Reddy, Gautam; Wong-Ng, Jerome; Celani, Antonio; Sejnowski, Terrence J.; Vergassola, Massimo.**  
*Glider soaring via reinforcement learning in the field.* Nature 562, 236–239 (2018).  
DOI: https://doi.org/10.1038/s41586-018-0533-0

**Why:** Broader precedent for flying RL-controlled gliders in the real world. Again, **thermal soaring**, not direct demonstration of shear-driven dynamic soaring.

## C. Technical implementation references

### [T1] ArduPilot Plane — soaring / thermalling

https://ardupilot.org/plane/docs/soaring-4_1.html

Shows practical glider airspeed and drag-polar considerations. Built-in soaring is for **thermal updrafts**, and must not be presented as a dynamic-soaring algorithm.

### [T2] ArduPilot — software in the loop

https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html  
https://ardupilot.org/dev/docs/sitl-with-jsbsim.html  
https://en.ardupilot.org/dev/docs/SITL_simulation_parameters.html

References for simulator/autopilot integration, external flight dynamics, control logs and wind perturbations. Verify wind-shear modeling instead of assuming the default wind controls generate a useful vertical velocity gradient.

### [T3] Transport Canada drone safety and registration

https://tc.canada.ca/en/aviation/drone-safety/flying-your-drone-safely-legally  
https://tc.canada.ca/en/aviation/drone-safety/registering-your-drone

Rules depend on operating weight, airspace and flight type; verify immediately before each test. Avoid reckless or hazardous conditions.

### [T4] Youth Science Canada CWSF judging information

https://help.youthscience.ca/portal/en/kb/articles/how-am-i-judged-at-the-canada-wide-science-fair

Present a defensible engineering question, measurements, evidence, and student contributions to both technical and interdisciplinary judges.

## D. Priority reading and reproduction tasks

1. **Start with [R5]/[R6]** for physically reasonable shear thresholds, energy balance and classical trajectory assumptions.
2. **Read [R1]** to reproduce one compact neural-feedback trajectory baseline.
3. **Read [R2]** to learn a practical policy/parameterization and fair optimizer comparison.
4. **Read [R3]** for AI + low-level control integration and robustness methods.
5. **Use [R4]** to prevent unrealistic endurance claims and model full powertrain costs.
6. **Treat [R7]/[R8]** as adjacent learning/engineering inspiration; avoid describing their thermalling results as dynamic soaring.

## E. Attribution and evidence policy

For each paper record: exact model, wind profile, equations, aircraft parameters, sensor/observation assumptions, constraints, training seeds if available, reported outcomes and any source code/data. Tag every claim as one of:
- **Published finding** with source.
- **Proposed hypothesis** (not yet tested).
- **Student reproduction result** with logs and conditions.
- **Student original modification and experiment** with version and evidence.

Do not redistribute copyrighted full texts into the repository without a suitable license. Links and short original summaries suffice.

## F. Additional papers from biological analogies and upwind soaring discussion (2026-10-18)

- **Richardson (2015)**, *Upwind dynamic soaring of albatrosses and UAVs*, Progress in Oceanography 130, 146–156. https://doi.org/10.1016/j.pocean.2014.11.002 — explicit Rayleigh-cycle modeling of upwind motion; closest citation for sailing/tacking analogy.
- **Richardson, Wakefield & Phillips (2018)**, *Flight speed and performance of the wandering albatross with respect to the wind*, Movement Ecology 6. https://doi.org/10.1186/s40462-018-0121-9 — observed flight and wind relationship.
- **Richardson & Wakefield (2022)**, *Observations and models of across-wind flight speed of the wandering albatross*, Royal Society Open Science 9, 211364. https://doi.org/10.1098/rsos.211364.
- **Lentink et al. (2007)**, *How swifts control their glide performance with morphing wings*, Nature 446, 1082–1085. https://doi.org/10.1038/nature05733 — experimental aerodynamic wing-sweep adaptation.
- **Jeger et al. (2024)**, *Adaptive morphing of wing and tail for stable, resilient, and energy-efficient flight of avian-inspired drones*, npj Robotics 2, 8. https://doi.org/10.1038/s44182-024-00015-y — physical bird-like morphing drone and open supporting data/code.
- **Weimerskirch et al. (2016)**, *Frigate birds track atmospheric conditions over months-long transoceanic flights*, Science 353, 74–78. https://doi.org/10.1126/science.aaf4374 — atmospheric navigation and convection.
- **Tucker (1995)**, *Drag reduction by wing tip slots in a gliding Harris' hawk*. https://doi.org/10.1242/jeb.198.3.775.
- **Miklosovic et al. (2004)**, *Leading-edge tubercles delay stall on humpback whale flippers*. https://doi.org/10.1063/1.1688341.
- **Cummins et al. (2018)**, *A separated vortex ring underlies the flight of the dandelion*. https://doi.org/10.1038/s41586-018-0604-2.

See [thermal vs. dynamic](08-thermal-vs-dynamic-soaring.md), [sailing analogy](09-sailing-upwind-and-dynamic-soaring.md), and [bio-inspired alternatives](../../ideas/bio-inspired-flight-research-options-2026-10-18.md) for discussion context, additional owl/dragonfly references and candidate experiments.
