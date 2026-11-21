# Albatross-Inspired Dynamic Soaring

## Consolidated science fair project brief

**CWSF 2027 · Christopher Lin · Updated October 23, 2026**
**Organization:** Inspiration by nature → Engineering → Applications
**Status:** Topic selected; research and engineering plan in development.
[Science fair entry point](README.md) · [AI and dynamic-soaring technical dossier][D0]

This document brings together the useful material already discussed in the CWSF 2027 project: albatross flight, dynamic-soaring physics, wing design, the standalone FSL investigations, the FW-01 aircraft concept, adaptive control, evaluation methods, and possible applications. It is a working reference for the selected science fair subject, not a report of completed experiments.

The synthesis uses the accessible conversation excerpts and retrieved conversation summaries, the repository at commit [`e68a0aa`](https://github.com/eugenelin89/cwsf2027-research/commit/e68a0aa8e64efded4847384308ea588543fe10cb), and direct readback of the two standalone FSL plans. The [source ledger](#sources-and-provenance) identifies those boundaries. No complete export of every historical chat was available.

**Contents:** [Direction and status](#project-direction-and-status) · [1. Nature](#1-inspiration-by-nature-albatrosses) · [2. Engineering](#2-engineering) · [3. Applications](#3-applications) · [Work plan](#work-plan-and-open-decisions) · [Reading map](#reading-map) · [Sources](#sources-and-provenance)

## Project direction and status

### The current project in one paragraph

Study how albatrosses exploit changing winds, translate the relevant physical principles into a small-aircraft engineering investigation, and evaluate what the demonstrated result could contribute to useful observation missions. The practical motivation is **endurance and useful distance with less propulsion energy or recharging**. Wing aerodynamics, structural mass and stiffness, flight trajectory, wind estimation, and adaptive control are connected design choices. The science fair needs a focused question within that larger system, with measurements that can support a clear conclusion. [C1], [C2], [C3], [D1]

The engineering direction carries forward the **Flight CWSF Ideas** combination: **AI-powered adaptive flight control (Idea 1) + albatross-inspired dynamic soaring (Idea 5)**. Its central question is whether adaptive control improves energy performance and robustness over credible conventional controllers under uncertain or changing winds. The three-part science fair structure organizes that combined concept alongside its wing-design and application context. Choosing the learning method, primary comparison, and feasible physical validation remains part of the engineering work. See the [conversation coverage map](#flight-cwsf-ideas-coverage-audit) for the detailed record. [C2], [I1], [D0], [D1]

### Decisions and proposals are different

| Item | Current interpretation | Basis |
| --- | --- | --- |
| Albatross-inspired dynamic soaring | **Selected science fair focus.** | Current user instruction, October 23, 2026. [C1] |
| Nature, engineering, applications | **Selected organizing structure.** | Current user instruction. [C1] |
| Endurance and distance | **Established preference** over a speed-record objective. | FSL/dynamic-soaring discussions. [C3] |
| Professional research | **Accepted foundation** for learning, engineering, reproduction, and comparison. | The student explicitly said prior professional work is not a reason to abandon the idea. [C2], [D7] |
| AI/adaptive control plus dynamic soaring | **Established combined concept carried forward into the engineering direction**, originally Idea 1 + Idea 5; a particular AI method is not yet fixed. | Flight CWSF Ideas and the combined idea note. [C2], [I1] |
| FW-01 flying wing | **Candidate physical platform**; suitability for dynamic soaring is unverified. | Aircraft and physics chapters. [D2], [D3] |
| Standalone FSL work | **Related component research**, with its own scope and deliverables. | User request and both FSL documents. [C3], [F1], [F2] |
| Specific application, primary endpoint, final hardware, total CWSF budget | **Open decisions.** | They are not fixed by the reviewed sources or the current topic decision. [D1], [D7] |
| Soaring performance, AI advantage, battery savings, completed physical tests | **Not established by this review.** | The source documents describe plans; no supporting project result files or measured outcomes were identified in the reviewed material. [D0], [F1], [F2] |

The earlier Idea 1 + Idea 3 combination concerned adaptive control and cooperative swarms. The user corrected that to **Idea 1 + Idea 5**. A swarm, rocket launch, or thermal-soaring search mission is therefore not a requirement of the selected project. Those earlier ideas remain useful historical context. [C2], [I1], [D7]

## 1. Inspiration by nature: albatrosses

### 1.1 The biological idea to explain

Albatross dynamic soaring uses differences in the velocity of air encountered along a flight path. Over the ocean, the wind close to the surface and in wave troughs can differ from the faster flow above. An appropriately oriented sequence of climbs and turns can extract energy from that difference. The engineering question is whether the energy gained can cover the aircraft's aerodynamic and maneuver losses. [P1], [P2], [P6]

For an idealized two-layer explanation:

1. The aircraft climbs toward the wind into faster-moving air; its velocity relative to the local air changes.
2. It turns in the upper layer.
3. It descends with the wind into slower-moving air, creating another favorable air-relative velocity change.
4. It turns in the lower layer and begins another cycle if the overall balance is favorable.

This is an introductory picture. Real trajectories depend on wind direction, shear shape, wave effects, aircraft performance, and maneuver limits. A brief increase in speed or altitude does not by itself prove a net energy gain over a whole cycle. The detailed energy-accounting requirements are in [D2].

**The energy comes from the atmosphere.** A strong, steady, uniform horizontal wind alone does not provide the same recurring wind-shear energy source for an unpowered cyclic maneuver. Sustained soaring also does not mean that onboard sensors, computing, communications, or actuators require no electrical power. [D2], [D4]

### 1.2 Translate the inspiration into engineering questions

| Natural feature or behavior | Engineering connection | Question to test |
| --- | --- | --- |
| Efficient gliding wings | Wing geometry, airfoil, drag, and lift-to-drag ratio | Does the proposed small wing have adequate performance at its actual size and speed? |
| Repeated turns and shear crossings | Maneuver energy and structural loads | Which cycles are energetically feasible without exceeding the modeled envelope? |
| Flight adapted to local wind conditions | Wind estimation and trajectory adaptation | Does adaptation help when the wind differs from the conditions used to design a fixed cycle? |
| Long-distance travel | Useful progress and mission energy | Does an energy-saving maneuver still advance the intended observation mission? |

These are translations of the inspiration into a research program, not evidence that a bird-shaped aircraft will work. For example, higher aspect ratio can reduce induced drag under comparable aerodynamic conditions, but the complete design also has structural, mass, fabrication, and operating constraints. [T1], [D2], [D3]

Richardson and Wakefield's 2022 work provides a particularly useful connection between flight behavior and wing loads. It compares observed flight with simplified models and proposes that birds adjust maneuvers partly to limit aerodynamic forces. **That explanation is a hypothesis in the paper, not a measured strength specification for albatross wings or printed UAV parts.** The FSL structural proposals use it as motivation for studying a load–mass tradeoff. [P6], [F1], [F2]

### 1.3 Dynamic soaring and thermal soaring

| Mechanism | Useful atmospheric feature | Typical behavior | Role here |
| --- | --- | --- | --- |
| **Dynamic soaring** | Differences in wind velocity across space | Cross the shear with coordinated climbs, descents, and turns | Selected physical mechanism. |
| **Thermal soaring** | Rising air | Circle within an updraft, then glide elsewhere | Related control and learning literature. |
| **Ridge / wave-slope soaring** | Air deflected upward by terrain or waves | Follow a region of lift | A separate effect that can coexist with shear and must be distinguished in observations. |

The earlier vulture-inspired paper, the field RL glider paper, and ArduSoar are relevant to sensing, learning, and validation, but they concern **thermals**. ArduPilot's documented soaring functionality also responds to rising air and centers thermals; enabling it does not implement this project's wind-shear controller. [P11], [P12], [P13], [T2], [D8]

### 1.4 The sailboat question from our discussions

The user asked how a sailboat can travel toward the wind and whether the same idea explains dynamic soaring. A sailboat makes upwind progress through angled tacks, using aerodynamic forces on its sails and hydrodynamic forces on its hull and keel. It interacts with air and water simultaneously. An albatross instead travels through air regions with different velocities; its inertia and trajectory allow energy exchange across the shear. The analogy is useful for explaining relative motion and upwind progress, but the force mechanisms differ. [D9], [P1], [P4]

### 1.5 What this part of the science fair should produce

The previously discussed material supports an explanation of the energy source, a labeled soaring cycle, a comparison with thermals, and a table connecting biological principles to engineering variables. A literature-to-design worksheet should record each adopted equation or design idea, its source, and which assumptions apply to the student aircraft. This is the foundation for the engineering evidence, not a claim to have conducted new biological observations. [D2], [D6], [F2]

## 2. Engineering

### 2.1 Candidate research questions already discussed

The established combined concept asks **under what wind uncertainty and aircraft-model mismatch conditions adaptive learned control improves on credible conventional dynamic-soaring control**. The earlier conversations also explored feasibility and wing structure as connected engineering questions. Select a manageable primary investigation within that combined direction and identify the supporting component work; the full question menu is not a set of simultaneous mandatory deliverables. [D1], [D4], [F1], [F2]

The recorded hypotheses allow a well-tuned classical method to match or outperform learning when its wind model is accurate; adaptation may help under changing or partly observed winds; and benefits may disappear when usable shear or aircraft efficiency is insufficient. A useful result is a measured or modeled map of **when adaptation helps and when it fails**. These are hypotheses to test, not established outcomes. [I1], [D1]

| Research direction | Testable question | Possible primary outcome |
| --- | --- | --- |
| **Soaring feasibility** | Which combinations of aircraft efficiency, maneuver constraints, and wind shear permit a useful complete cycle? | Net cycle energy or the modeled minimum usable shear under a defined task. |
| **Wing structure** | Can a model-guided spar design reduce panel mass while meeting the same bending requirement? | Measured mass reduction conditional on load compliance, plus prediction error. |
| **Adaptive control** | Does adaptation improve performance under uncertain or changing winds compared with credible conventional methods? | A predeclared energy measure, with completion and constraint violations reported. |
| **When to soar** | Can a supervisor avoid energy-wasting soaring attempts when conditions are unsuitable? | Energy used for a common mission, including switching and recovery. |

The student has emphasized designing, building, understanding, and testing. Existing professional work is a reference and a benchmark. A useful contribution could be a carefully implemented reproduction, a measured design tradeoff, a controller comparison, a map of failure conditions, or a bounded negative finding. Originality should be stated at that specific level. [C2], [D7]

### 2.2 Wing aerodynamics and the earlier phase plans

The FSL conversations originally considered an aerodynamic sequence: research dynamic soaring, choose five existing airfoils, model them in Autodesk Fusion, use XFLR5/flow5 for initial comparisons, fabricate prototypes, and then develop structural and mass improvements. The phase labels evolved: one version used **airfoil research → structural integrity → weight optimization**, while a later template used **airfoil research → wing geometry → lightweight structural optimization**. These are related planning versions, not a single frozen protocol. [C3], [C4]

Useful design quantities include airfoil shape, span, chord, wing area, aspect ratio, mass, wing loading, center of gravity, lift-to-drag ratio, and the speed range relevant to the intended aircraft. A drag polar describes how drag changes with lift; it is a more useful model input than assuming one optimistic glide-ratio number for every maneuver. [D2], [D3]

An assistant suggestion in the later Phase 1 discussion was a controlled NACA 0012 / 2412 / 4412 camber comparison at illustrative Reynolds numbers of 100,000, 150,000, and 200,000. **These were candidate screening cases, not the selected five airfoils or a verified FW-01 operating range.** Actual dimensions and airspeeds must determine the relevant conditions. If camber is the variable, hold the other geometry and comparison conditions fixed. [C4]

XFLR5 is intended for airfoil, wing, and aircraft analysis at low Reynolds numbers; flow5 is a potential-flow tool. Their outputs remain model predictions with method assumptions. The earlier preference was to keep advanced CFD and finite-element analysis optional. Neither software plots nor a simple airflow demonstration establish measured lift and drag without suitable measurement and calibration. [T3], [C3], [C4]

**Tool-status check, October 23, 2026:** The official XFLR5 page states that its project closed on June 30, 2026, with no further releases, and identifies flow5 as its successor. The earlier XFLR5/flow5 planning references are retained; the actual tool and version should be recorded when chosen. [T3]

### 2.3 The FSL work: two documented structural investigations

The user asked for FSL to stand alone and later asked for a more advanced Grade 11 investigation closer to dynamic soaring. Both resulting documents were read directly for this consolidation. They are planning drafts dated October 19, 2026. [C3], [F1], [F2]

| Version | Main experiment | How it can inform the science fair |
| --- | --- | --- |
| **Wing Mass and Bending Response for Albatross-Inspired Dynamic Soaring** | Keep a representative panel's outer geometry fixed; compare spar thickness, mass, and bending response under a documented bench requirement. | Establish a repeatable component-testing method and the distinction between mass, stiffness, and strength. [F1] |
| **Model-Guided Wing Design for Dynamic Soaring: Predict, Redesign and Test** | Reproduce a reduced soaring model, connect representative maneuver loads to a beam model, predict a redistributed spar, then test independent specimens against a fair uniform comparator. | Connect nature, calculation, engineering prediction, fabrication, and physical evidence. [F2] |

The shared first deliverable is deliberately modest: one printable baseline, a checked fixture, pilot measurements, and a repeatable method. The advanced proposal adds a model and independent prediction test later. It excludes CFD, a full three-dimensional flight simulator, AI training, aircraft integration, and outdoor soaring from **FSL completion requirements**. Those exclusions do not decide the entire CWSF scope. [F1], [F2]

#### Proposed advanced design-and-test sequence

1. **Reproduce:** Check a compact published two-layer soaring model and map how turn angle and cycle duration affect wind requirements, representative loads, and useful across-wind progress.
2. **Calibrate:** Test three independently printed uniform-spar specimens and fit a simple beam model, checking fixture motion separately.
3. **Predict:** Search a small family of uniform and tapered spars under common loads and deflection limits. Size the uniform comparator fairly.
4. **Freeze:** Save the selected CAD, predicted mass and deflections, acceptance limits, and model version before inspecting final validation results.
5. **Fabricate and test:** Produce three fresh uniform-comparator specimens and three fresh redesigned specimens. Test both with the same selected load cases and timing.
6. **Explain:** Report measured mass, compliance, residual deformation, prediction errors, uncertainty, failed specimens, and reasons the model did or did not transfer.

This is the **proposed** nine-specimen research allocation—three calibration plus six validation specimens—with a separate pilot allowance. Repeating a reading or load sequence three times on one panel does not create three independent specimens. The final counts depend on printing access and material use; no specimens or results are claimed here. [F2]

The advanced structural design changes the **chordwise width distribution of a rectangular spar while holding its vertical depth fixed**. This is not a change to aerodynamic wing taper. The outer panel geometry, ribs, attachments, material, print settings, fixture, and load positions stay controlled. The proposed first article is an open spar-and-rib component without a continuous load-bearing skin. [F2]

#### What to measure and what it means

| Measurement | Use | Interpretation limit |
| --- | --- | --- |
| Panel mass; spar mass where separable | Compare material efficiency | A percentage reduction in panel mass is not the same percentage reduction in aircraft mass or increase in endurance. |
| Applied force and lever arm | Define loading and bending moment | A point load or matched root moment does not reproduce the full distributed aerodynamic load. |
| Tip deflection and residual deflection | Check a common bench requirement | Elastic stiffness is not failure strength, flutter resistance, fatigue life, or flight certification. |
| Frozen prediction versus fresh-specimen response | Test model transfer to a changed geometry | Refitting after seeing validation data creates a later exploratory model, not independent validation of the original prediction. |

The advanced draft proposes three preselected load cases, three non-damaging technical repeats, and a provisional prediction target near 20% error at a reference case, with an absolute-error alternative near instrument resolution. These are proposed choices to review and freeze after the pilot, not universal standards. [F2]

#### Load and beam calculations already discussed

For reference aircraft mass $m$, lift $L$, gravity $g$, and load factor $n$:

$$n=\frac{L}{mg}, \qquad L=nmg.$$

In an ideal steady level banked turn, $n=1/\cos\phi$, where $\phi$ is bank angle. This approximation does not supply peak loads during a shear crossing, gust, or rapidly changing maneuver. A fixture point force $F$ at distance $a$ gives root moment $M=Fa$, but a matching moment alone is not complete load equivalence. [P6], [F1], [F2]

For a rectangular spar of width $w$ and fixed vertical bending depth $h$, $I=wh^3/12$. A uniform cantilever with a tip load provides the beam-code check $\delta=F\ell^3/(3E_{\mathrm{eff}}I)$. The effective bending parameter is fitted for the specimen and model; it is not a certified material property. Tapered sections and multiple load stations require the appropriate moment–curvature calculation and a discretization check. [T4], [F2]

#### Budget, equipment, and access

The **under-$80 CAD limit belongs to the FSL component study**. The standalone drafts propose $60 in supply allowances plus $15 contingency, giving a $75 planning cap. This is not the full CWSF aircraft budget or a record of purchases. [F1], [F2]

Approximately 500 g of PLA and access to a 3D printer were confirmed in the original template. A later template discussion listed a digital scale and force gauge as available, whereas the standalone plans still require measurement and fixture resources to be confirmed. Record actual access and resolution before scheduling tests. Carbon-fiber rods—3 mm × 500 mm, a pack of ten at a historical quoted price of about $16.49 CAD—were discussed in an earlier reinforcement plan; that is not a current price check, a confirmed purchase, or a requirement of the printed-spar redesign. [C4], [F1], [F2]

### 2.4 A small soaring model before a full simulator

The advanced FSL draft proposes the Richardson–Wakefield two-layer model as a tractable first calculation. Its radian-form equations can be written using **$\alpha$ for the amplitude of each turn** and $T_c$ for the duration of the complete two-turn cycle:

$$\Omega=\frac{2\alpha}{T_c}, \qquad n=\sqrt{1+\left(\frac{\Omega V}{g}\right)^2},$$

$$W_{\mathrm{req}}=\frac{gT_c}{4G\sin(\alpha/2)}\left[\left(\frac{V}{V_c}\right)^2+\left(\frac{V_c}{V}\right)^2+\left(\frac{\Omega V_c}{g}\right)^2\right],$$

$$V_{\mathrm{across}}=V\frac{2\sin(\alpha/2)}{\alpha}.$$

Here $V$ is mean airspeed, $V_c$ is straight-flight minimum-drag airspeed, and $G$ is maximum straight-flight glide ratio. $W_{\mathrm{req}}$ is a **wind-speed difference in m/s between idealized layers**, not the gradient $dW/dz$ in s⁻¹. The lower layer is at rest in that model. [P6], [F2]

For the reference case $V=V_c=16$ m/s, $G=21.2$, $\alpha=90^\circ$, and $T_c=10$ s, the equations give approximately **3.70 m/s required layer contrast, 1.12 representative load factor, and 14.4 m/s across-wind airspeed component**. These are reference-model calculations, not student measurements, FW-01 predictions, or the minimum over all possible maneuvers. The $90^\circ$ angle must be converted to radians. [P6], [F2]

The FSL draft's proposed parameter exploration was turn angles of 30–150° and cycle durations of 6–14 seconds. It would require a declared progress constraint and grid refinement; a best grid point is not proof of a global optimum. Keep published bird parameters and assumed UAV parameters in separate sheets. This calculation uses averaged turns and idealized shear, so it cannot validate a deployable controller or determine peak structural loads. [F2]

For a later control investigation, the earlier repository plan proposes a three-dimensional point-mass simulator with explicit lift/drag, wind field, actuator/maneuver limits, and reproducible initial conditions. A six-degree-of-freedom model or flight-controller simulation should be added only where necessary for the claim being tested. ArduPilot SITL and JSBSim are candidate integration tools; their configured wind field must actually represent altitude-dependent shear. [D2], [D3]

### 2.5 Energy accounting: keep the quantities distinct

For ground velocity $\mathbf v_g$, local wind $\mathbf W$, air-relative velocity $\mathbf v_a$, and altitude $z$:

$$\mathbf v_a=\mathbf v_g-\mathbf W,$$

$$E_g=mgz+\tfrac12m|\mathbf v_g|^2, \qquad E_a=mgz+\tfrac12m|\mathbf v_a|^2.$$

$E_g$ is ground-frame mechanical energy; $E_a$ is an air-relative diagnostic. They are different quantities in a varying wind field. Both are total energies in joules; divide by mass to obtain specific energy. Wind-work terms and coordinate conventions must be explicit. [D2]

Electrical energy is a separate measurement:

$$E_{\mathrm{battery}}=\int V_{\mathrm{battery}}(t)I(t)\,dt.$$

Integrating watts over seconds gives joules; divide by 3,600 for watt-hours. A controller reward, a temporary altitude gain, reduced commanded throttle, or a faster ground track is not automatically a measurement of saved battery energy. Avionics, propulsion efficiency, recovery, and transitions matter for a whole mission. [D4], [P10]

Compare complete cycles or task-matched missions. Specify the starting conditions and acceptable ending altitude, speed, direction, location/progress, and time constraints. It is possible to obtain an apparent benefit simply by ending lower or slower; that must be accounted for rather than labeled harvested energy. [D2], [D4]

The existing verification sequence is: still-air glide with drag losses; steady uniform-wind control; a known shear case; timestep convergence; enforced maneuver constraints; and reproduction of an appropriate published baseline. These checks precede learning or performance claims. [D2], [D4]

### 2.6 FW-01 and the physical aircraft track

The earlier project discussed a roughly **85 cm 3D-printed flying wing** with carbon reinforcement, hand launch, and belly landing. Its span and an approximately 15-minute endurance objective were planning context, not measured performance. Discussions also considered LW-PLA, Raspberry Pi 5 / ESP32 hardware, servo options, batteries, motor/ESC/propeller combinations, RC links, MAVLink, and CRSF. Shopping discussions must not be treated as a verified bill of materials. [C5], [D3]

Before using FW-01 parameters in the science fair, establish the actual design revision, all-up mass, wing area, center of gravity, powertrain, controls, sensor set, glide behavior, and uncertainty. The repository specifically warns that a small flying wing may have insufficient glide efficiency or excessive turn losses for useful physical dynamic soaring. A more efficient glider remains a possible design choice. FW-01 can still support conventional glide measurements or model validation if it cannot sustain energy-positive soaring. [D2], [D3]

Candidate instrumentation functions are attitude/acceleration sensing, altitude, ground velocity, airspeed, battery voltage/current, and synchronized logs. **Groundspeed is not airspeed.** The plan discusses an airspeed sensor for better wind and glide estimates, but this brief does not select or purchase hardware. RC pilot control, telemetry/mission communication, and optional video have different functions; MAVLink and CRSF are not interchangeable names for every link. [D3], [T2]

Physical evidence should be linked to the exact claim: a bench panel validates component response; an ordinary glide informs an aerodynamic model; software-in-the-loop tests an integration path; a real wind-shear maneuver would require its own evidence. The earlier scope permits rigorous simulation plus selected physical validation without making outdoor dynamic soaring a mandatory milestone. [D3], [D7]

**Aircraft design sequencing, documented November 12, 2026:** the [aircraft design and test plan](aircraft-design-and-test-plan.md) develops a preliminary complete-aircraft layout alongside construction-coupon testing. The layout can establish candidate equipment placement, geometry, and mass/CG estimates before a coupon is printed. Measured fit/mass and appropriate aerodynamic/structural analysis inform the final dependent details. This is a planning decision, not a completed aircraft or validation result; [CAD-002](cad-decisions.md#cad-002--develop-the-complete-aircraft-layout-alongside-coupon-testing) records its scope.

### 2.7 Adaptive control and comparison methods

The earlier architecture separates a conventional low-level flight controller from a higher-level adaptive method that chooses bounded trajectory, bank, airspeed, altitude, or mode references. A supervisor checks the modeled envelope and provides a conventional fallback. The first learned method operates in simulation. [D3]

Previously discussed approaches include imitation of optimized trajectories, reinforcement learning over a compact trajectory description, learned feedback, and a supervisor that chooses whether to soar. These methods are not identical: Kim et al.'s neural feedback is trained on optimized state–control pairs; Zou et al. use a reinforcement-learning trajectory method. The chosen algorithm must follow the research question and available validation effort. [P7], [P8], [P9], [D2]

| Previously proposed comparator | What it helps establish |
| --- | --- |
| Ordinary glide or powered cruise | Energy/useful progress without intentional dynamic soaring, for a carefully matched task. |
| Fixed precomputed cycle | Whether adapting to conditions adds value. |
| Optimized trajectory with conventional tracking | Comparison with a strong model-based method. |
| Robust/adaptive classical controller | Whether learning adds value beyond conventional adaptation. |
| Learned controller | Performance of the proposed adaptive method under the same constraints and observations. |
| Always-soar versus conditional soar/glide/powered switching | Optional test of deciding when soaring is worthwhile. |
| Perfect-wind oracle | A clearly labeled diagnostic upper bound, not a fair deployable competitor. |

This is a menu retained from the earlier plan, not a commitment to implement every method. The useful initial study is the smallest comparison that answers the chosen question. Methods need comparable sensing, constraints, tuning opportunities, and mission objectives. [D4]

### 2.8 Variables, measurements, and reliability

| Experiment family | Independent variables already proposed | Dependent measurements | Essential controls |
| --- | --- | --- | --- |
| Airfoil screening | Airfoil/camber at defined operating conditions | Predicted lift, drag, lift-to-drag ratio | Geometry, Reynolds number, solver settings, angle/speed comparison. |
| Structural comparison | Spar thickness or width distribution; choose one protocol | Mass, force–deflection response, residual deformation, prediction error | Outer geometry, print/material settings, fixture, loads, timing. |
| Soaring feasibility | Wind shear or layer contrast, aircraft polar, maneuver parameters | Complete-cycle energy, usable-shear boundary, task progress | Aircraft model, envelope, initial state, energy convention. |
| Controller comparison | Method and wind-estimation uncertainty | Mission/cycle energy, completion, violations, robustness, compute time | Same test winds/seeds, observations, aircraft, task, and termination rules. |

Sources: [C4], [F1], [F2], [D2], and [D4].

The earlier simulation plan suggested at least 20 paired wind conditions and, when learning is used, at least three independent training seeds as practical starting targets. These are not completed runs, a statistical power calculation, or automatically sufficient replication. Training, tuning, and final test conditions should be separate; freeze the final method before evaluation and retain failed episodes. [D4]

Report the primary metric, specimen/trial variation, measurement resolution, uncertainty, exclusions, and failure rates. Numerical grid points and timestep checks are different from independent physical specimens or independent wind realizations. Keep raw evidence linked to CAD/model versions and exact conditions. [D4], [F2]

The earlier notebook structure is reusable: problem, prediction, methods, variables, controlled conditions, trial/seed count, raw evidence, uncertainty, interpretation, and next decision. Log assistance and distinguish published methods from the student's design, implementation, and measurements. [D5], [D6]

## 3. Applications

### 3.1 Applications discussed so far

The earlier conversations showed interest in aerospace combined with environmental sensing and biological or marine monitoring. The repository connects dynamic soaring with lower-energy observation missions. **A final mission, sensor payload, species, environmental variable, or end-user has not been selected in the reviewed sources.** [C2], [C3], [C6], [D1]

| Application candidate | Possible value of a demonstrated soaring benefit | Measurements needed to support the application | Current status |
| --- | --- | --- | --- |
| **Environmental sensing** | More useful coverage or measurements for a given energy budget | Energy, area, duration, and a task metric such as field-reconstruction error or information gained | Earlier concept included temperature/humidity fields, synthetic first and measured where feasible. [I2] |
| **Coastal / ocean observation** | Longer useful observation or less propulsion on suitable windy routes | Common route and payload, useful observation time, wind conditions, propulsion/avionics costs, and return/recovery assumptions | Motivation in the dynamic-soaring proposal; ocean deployment is outside its initial scope. [D1] |
| **Marine wildlife survey** | Survey coverage or detection performance under a common energy budget | Coverage, missed detections, precision/recall, energy, and any clearly identified disturbance proxy | Earlier concept uses simulation and licensed/permissioned imagery; no animal-disturbance experiment is established. [I3] |
| **Wind-adaptive autonomous flight** | Choosing a more effective flight mode as wind opportunities change | Mission energy, useful progress, completion, and failures relative to a common baseline | Previously proposed supervisor investigation. [D1], [D4] |
| **Upwind survey travel** | Progress toward observations while using favorable shear | Net route progress, travel time, energy and transition costs | Discussed through the sailing analogy and idealized upwind models. [D9], [P1] |

These are candidate uses, not achieved outcomes. A longer flight becomes an application benefit only if it produces useful observations or task progress. More time circling can be a poor survey result if it reduces coverage or misses the observation window. The earlier environmental-sensing idea therefore measured information or reconstruction quality alongside energy. [I2], [D4]

### 3.2 A defensible connection from experiment to application

Use the project's actual evidence level to set the strength of the claim:

| Evidence produced | Application statement it can support |
| --- | --- |
| A lighter panel meets the chosen bench requirement | A measured component-design tradeoff under the tested loading. Whole-aircraft benefits remain to be evaluated. |
| A verified model predicts favorable energy cycles for a stated airframe and wind | Conditional feasibility in that model and parameter range. |
| A controller improves a frozen simulated mission comparison | A modeled mission benefit under the tested sensing, dynamics, and wind assumptions. |
| Calibrated physical power and flight measurements support a common mission comparison | A bounded measured benefit for those aircraft, conditions, and tasks. |

This distinction follows the existing structural and flight plans. It prevents the project from treating model output as field deployment, or panel mass savings as battery endurance. [F2], [D4], [P10]

Before selecting an application experiment, define the observation objective, the common route or coverage requirement, the sensing quality required, and the wind and energy budget. Use a relevant baseline: the earlier environmental proposal includes lawnmower coverage, greedy sampling, and energy-aware planning; the marine proposal includes fixed-altitude surveys and uniform transects. Those comparisons belong to an application study if selected; they need not all be added to the core soaring experiment. [I2], [I3]

### 3.3 Earlier directions to keep as background

The September information-foraging and cooperative-search discussions introduced a useful question: **what scientific information does the aircraft help obtain?** That principle transfers to the applications section. Their balloons, swarms, occlusion-search algorithms, rocket-assisted launch, and thermalling missions do not transfer automatically as implementation requirements. Likewise, the later humanitarian-protection brainstorming is an older unselected branch, not the current application choice. [C6], [I4], [I5]

## Work plan and open decisions

### Consolidated progression

The three-part science fair story is an organizing structure, not three isolated chronological projects. Biology informs the engineering; an intended application helps define the engineering metric. The prior plans support the following progression, with scope chosen to match the primary question. [D5], [F2]

| Stage | Useful output | Evidence needed before progressing |
| --- | --- | --- |
| Establish the mechanism and objective | Literature-to-design worksheet; one primary question and metric | Correct distinction between wind shear, updrafts, and energy measures. |
| Establish a baseline | Known model calculation; baseline CAD/fixture or characterized aircraft | Reproducible model behavior and measurements appropriate to the chosen track. |
| Predict or implement a change | One spar redesign, maneuver change, or controller comparison | A saved prediction/protocol and a fair comparator. |
| Evaluate independently | Fresh specimens or held-out wind/mission trials | Common conditions, uncertainty, failures, and traceable raw data. |
| Interpret application value | A bounded observation/mission argument or optional scenario test | The application claim stays within the measured or simulated evidence. |
| Prepare the science fair record | Methods, figures, demonstration, notebook, attribution, and limitations | Clear separation of published, proposed, simulated, bench, and flight evidence. |

For the engineering work within this progression, use the [parallel aircraft design and test plan](aircraft-design-and-test-plan.md) and [Work prompt register](../prompts/README.md). A preliminary layout task does not have to wait for every physical coupon observation. The research baseline and fair-comparison requirements above remain in effect.

### Dates retained from prior planning

- **November 24, 2026:** FSL trial run, approximately two hours, intended for baseline and method checks.
- **December 1, 2026:** FSL trial run, approximately 1.5 hours; proposed baseline CAD, fixture, pilot data, and repeatable-method checkpoint.
- **January–February 2027:** the advanced FSL draft proposes model checks, calibration, frozen predictions, fresh-specimen testing, and analysis.
- **March 2 and March 9, 2027:** proposed FSL evidence-review and report/demo preparation sessions.
- The earlier CWSF dossier has approximate October–April aircraft/model/control milestones. They remain planning targets. Official regional-fair, CWSF, and FSL submission deadlines were not verified by this consolidation and should not be inferred from that roadmap.

Sources: [F1], [F2], and [D5]. These dates are not completion records or newly confirmed program deadlines. The earlier airfoil-first discussion had a different October–December work sequence; the structural drafts should not silently overwrite that history. [C4]

### Decisions to resolve next

| Decision | Why it matters | Evidence to use |
| --- | --- | --- |
| Primary engineering claim | Sets what must be built and measured | Select a bounded claim within the combined flight-control/soaring direction and define how feasibility and structural measurements support it. |
| Main outcome and fair task | Mechanical energy, electrical energy, endurance, and useful distance require different comparisons | Existing physics and experiment definitions. [D2], [D4] |
| Component / airframe choice | A test panel and a complete aircraft support different claims | Inventory, actual geometry/mass, available instrumentation, and aerodynamic feasibility. |
| AI task and method | Focuses the combined concept on a testable control problem | Choose trajectory adaptation, learned feedback, or supervisory switching; reproduce a conventional method and identify the uncertainty to test. |
| Application scenario | Gives energy/endurance a useful mission meaning | Environmental or marine task requirements and feasible data access. |
| Budget, time, and physical validation | Determines a realistic scope | Separate the FSL allowance from aircraft needs and verify actual access. |

**Immediate priorities carried forward from the discussions:** establish the actual inventory and available test setup; reproduce one suitable physics baseline; and write down one primary metric and comparison before expanding the AI or fabrication work. [D7], [F2]

## Reading map

### Previously discussed papers, organized by purpose

The entries below are a curated route into the existing bibliography. They are not claims that the student has read or reproduced every paper. Publisher abstracts, author/institutional records, and accessible full texts were used selectively to check the references; the detailed prior annotations remain in [D6].

| ID | Paper and link | Why it is useful here |
| --- | --- | --- |
| **P1** | Richardson (2015), [*Upwind dynamic soaring of albatrosses and UAVs*][P1] | Albatross/UAV mechanism, upwind travel, and mission-specific design context. |
| **P2** | Sachs (2005), [*Minimum shear wind strength required for dynamic soaring of albatrosses*][P2] | Complete-cycle feasibility and maneuver/load constraints. |
| **P3** | Deittert et al. (2009), [*Engineless Unmanned Aerial Vehicle Propulsion by Dynamic Soaring*][P3] | Conventional trajectory optimization and a classical reference. |
| **P4** | Sachs (2016), [*In-flight measurement of upwind dynamic soaring in albatrosses*][P4] | Observed bird flight and upwind interpretation. |
| **P5** | Richardson, Wakefield & Phillips (2018), [*Flight speed and performance of the wandering albatross with respect to wind*][P5] | Field observations of flight in relation to wind; Movement Ecology 6, article 3. |
| **P6** | Richardson & Wakefield (2022), [*Observations and models of across-wind flight speed of the wandering albatross*][P6] | The reduced model and proposed maneuver-load connection used in the advanced FSL draft. [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9709578/). |
| **P7** | Kim et al. (2019), [*Deep Neural Network-Based Feedback Control for Dynamic Soaring of Unpowered Aircraft*][P7] | Optimizer-derived neural feedback; distinct from reinforcement learning. |
| **P8** | Zou et al. (2025), [*A novel trajectories optimizing method for dynamic soaring based on deep reinforcement learning*][P8] | PPO and parameterized-trajectory comparison with conventional optimization. |
| **P9** | Lu, Xie & Ji (2025), [*Human-in-the-loop reinforcement learning for dynamic soaring: A trajectory planning and control integrated system*][P9] | Connecting planning and lower-level control; do not infer a field demonstration from simulation. |
| **P10** | Sun et al. (2026), [*Enhancing UAV endurance: coupled optimization of dynamic soaring trajectory and high-fidelity powertrain energy management*][P10] | Whole-mission propulsion and transition accounting; published gains are scenario-specific. |
| **P11** | Reddy et al. (2018), [*Glider soaring via reinforcement learning in the field*][P11] | Physical RL glider evidence for **thermal** soaring. |
| **P12** | Flato et al. (2024), [*Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning*][P12] | Bird-inspired learning and robustness in **thermals**. |
| **P13** | Tabor, Guilliard & Kolobov (2018), [*ArduSoar: an Open-Source Thermalling Controller for Resource-Constrained Autopilots*][P13] | An implementation reference for **thermalling**, not a dynamic-soaring controller. |

**Suggested order:** P1/P2 for mechanism and feasibility; P6 for the compact nature-to-engineering model; P3 for conventional flight-trajectory work; then P7–P9 to choose and scope the adaptive-control method. P10 informs mission-energy accounting. P11–P13 remain adjacent references rather than evidence of the selected physical mechanism. [D6], [F2]

Supplementary sources already used in the FSL plans or tool discussions:

- [NASA Glenn: induced drag and aspect ratio][T1].
- [MIT OpenCourseWare / Roylance: Beam Displacements][T4].
- [Chacón et al. (2017): PLA additive-manufacturing process parameters and mechanical properties][T5]. Treat fabrication settings as controls; do not import a modulus without matching and validating the method.
- [ArduPilot soaring documentation][T2] and [SITL documentation](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html).
- [XFLR5 official introduction][T3] and [flow5 official site](https://flow5.tech/).

Other natural flight mechanisms—swift morphing, owl flight, hawk wingtip slots, dragonfly corrugations, whale tubercles, frigatebird uplift, and flying seeds—remain in the [bio-inspired flight options note][I6]. They are background alternatives, not extra requirements for the albatross project.

## Sources and provenance

### Conversation sources

Conversation evidence was recovered from the project context and targeted conversation summaries. Stable chat URLs were not returned, so titles and discussion dates are recorded rather than invented links. Dates spanning October 18–19 reflect the discussion sequence and differing timestamp representations; document dates are preserved as written.

| ID | Conversation / date | Information carried forward |
| --- | --- | --- |
| **C1** | Current user instruction, October 23, 2026 | Select dynamic soaring inspired by albatross; organize as nature, engineering, applications; create this repository entry folder. |
| **C2** | **Flight CWSF Ideas**, October 18–19, 2026 | Correct Idea 1 + 3 to Idea 1 + 5; combine adaptive control and dynamic soaring; accept prior research; ask about thermal soaring, sailing, and references. |
| **C3** | **FSL**, October 18–19, 2026 | Endurance/distance preference; standalone FSL requirement; under-$80 context; manageable methods; request a more advanced model/design investigation. |
| **C4** | **Split Project Into Phases** and project-plan discussion, October 19, 2026 | Five-airfoil/Fusion/XFLR5-flow5 proposal; evolving phase labels; materials and trial dates; teacher-scoped baseline, test, and data plan. |
| **C5** | **Plan Flying Wing UAV**, September 23 onward, plus **Organize Lab Notebook**, October 8, 2026 | FW-01 planning context, hardware/communication questions, and a notebook organized around problems, hypotheses, variables, and success criteria. |
| **C6** | **Design Notebook Thesis**, September 2; **Swarm Robotics Ideas**, September 9; **War Room**, September 17 onward | Scientific-instrument and environmental/biological-monitoring motivation; earlier aerospace, swarm, search, and thermal-soaring ideas. |

### Flight CWSF Ideas coverage audit

**Checked October 23, 2026, following the user's question about completeness.** A targeted retrieval reconfirmed the Idea 1 + Idea 5 correction, the engineering-first preference, the uncertain-wind controller comparison, broad methods and metrics, simulation/physical-validation scope, references, and the thermal-soaring and sailing explanations. The available evidence consists of selected messages and conversation summaries; a complete thread transcript was not available. No substantive omission was identified among those retrieved points, but this is not a certification that every sentence or detail of the full conversation has been archived.

The following map locates both the reconfirmed discussion points and the fuller implementation proposals already recorded in the repository. It does not imply that each implementation detail was independently recovered verbatim from the conversation.

| Discussion area | Details preserved in the repository | Detailed location |
| --- | --- | --- |
| **Intended combination** | Idea 1 is AI-powered adaptive flight control; Idea 5 is albatross-inspired dynamic soaring. The user's correction from the earlier 1 + 3 swarm combination is explicit. | [Combined idea][I1]; [dossier overview][D0]. |
| **Engineering-first purpose** | Learn from professional research; build, understand, reproduce, experiment, and improve. Record the student's design, implementation, measurements, and contribution. Existing prior art is an accepted foundation. | [Overview][D0]; [proposal][D1]; [story and decisions][D7]. |
| **Research question and hypotheses** | Test when adaptation helps under uncertain/changing wind and model mismatch; identify minimum feasible shear and aircraft efficiency; allow a classical controller to match or outperform AI. The optional supervisor asks when soaring is worthwhile. | [Combined idea][I1]; [proposal and hypotheses][D1]. |
| **Physics and simulation** | Wind gradients, lift/drag models, complete-cycle energy, reference frames, maneuver limits, still-air and uniform-wind checks, timestep convergence, and reproduction of a published baseline. | [Physics and modeling][D2]; [evaluation sequence][D4]. |
| **Candidate AI methods** | Neural feedback learned from optimized trajectories, imitation learning, reinforcement learning including PPO, wind-history or belief-state observations, and optional soar/glide/powered-flight decisions. These are proposals; no final algorithm has been selected. | [Combined idea][I1]; [modeling][D2]; [architecture][D3]; [references][D6]. |
| **Aircraft and control architecture** | FW-01 as a candidate; measured aerodynamic parameters; IMU/barometer, GNSS, airspeed and voltage/current sensing; conventional low-level stabilization, bounded high-level adaptation, a supervisor, fallback, manual override, telemetry, and logging. | [Aircraft and control architecture][D3]. |
| **Comparison methods** | Ordinary glide/powered cruise, fixed soaring cycle, model-based optimized trajectory with tracking, robust/adaptive classical control, and learned control. Optional always-soar versus conditional switching; perfect-wind oracle labeled separately. | [Five-method comparison and optional variants][D4]. |
| **Variables and fair evaluation** | Shear strength/profile, turbulence, wind-estimation error, sensor noise/delay, model mismatch and aircraft efficiency; comparable observations, constraints, starting/ending states and tasks; held-out paired wind cases, independent training seeds and recorded failures. | [Experimental design][D4]; [combined idea][I1]. |
| **Measurements and ablations** | Complete-cycle mechanical energy, electrical energy, energy per distance, endurance, tracking, completion, violations and compute latency. Ablations test wind history, memory, domain randomization, supervision, switching, and aircraft-model accuracy. | [Metrics, repeatability, and ablations][D4]. |
| **Build and validation scope** | Parallel aircraft and simulator work; characterize real glide/power behavior; software-in-the-loop and conditional hardware-in-the-loop; real outdoor dynamic soaring is an optional extension. A small FW-01 may not support positive net soaring energy. | [Overview][D0]; [architecture][D3]; [roadmap and notebook][D5]; [risks and fallbacks][D7]. |
| **Applications and success criteria** | Environmental and coastal/marine observation, reduced propulsion demand and wind-adaptive flight are motivations. A final mission is open; a well-supported failure threshold or no-AI-advantage result remains useful. | [Proposal][D1]; [experiments][D4]; [story and decisions][D7]. |
| **Research papers and related explanations** | Richardson, Sachs and Deittert; Kim's neural feedback, Zou's RL trajectories, Lu's integrated planning/control, Sun's powertrain/trajectory work; adjacent thermal-soaring papers; thermal/dynamic distinction and the sailboat analogy. | [Annotated bibliography][D6]; [thermal comparison][D8]; [sailing and upwind flight][D9]. |

**Documentation correction from this audit:** the science fair README previously described AI as a “possible engineering component,” which understated the established combined concept. The entry point and this brief now explicitly carry forward **AI-powered adaptive flight control + albatross-inspired dynamic soaring**. This clarifies the record while leaving the algorithm, primary experiment, aircraft and application open.

### Directly reviewed FSL documents

| ID | Document | Review boundary |
| --- | --- | --- |
| **F1** | [Standalone wing mass and bending response plan][F1] | Native document text read on October 23, 2026; dated October 19; planning draft with no claimed completed tests. |
| **F2** | [Advanced model-guided wing design plan][F2] | Native document text read on October 23, 2026; dated October 19; includes reduced equations, proposed independent specimens, and explicit interpretation limits. |

The FSL documents are linked as source material and were not rewritten by this consolidation. The later template's equipment statements and the drafts' “confirm access” entries remain distinguishable.

### Repository source map

| IDs | Existing source | Contribution to this brief |
| --- | --- | --- |
| **D0–D2** | [Dossier overview][D0], [proposal][D1], [physics][D2] | Original objective, hypotheses, scope, energy accounting, and feasibility. |
| **D3–D5** | [Architecture][D3], [experiments][D4], [roadmap/notebook][D5] | Hardware/control roles, baselines, measurements, replication, and recording. |
| **D6–D9** | [Annotated references][D6], [story/decisions][D7], [thermal comparison][D8], [sailing analogy][D9] | Literature, engineering philosophy, history, and physical distinctions. |
| **I1–I3** | [Combined concept][I1], [environmental sensing][I2], [marine monitoring][I3] | Idea 1 + 5 provenance and candidate application questions. |
| **I4–I6** | [Information-foraging observatory][I4], [idea index][I5], [bio-inspired alternatives][I6] | Earlier motivation and background alternatives. |
| **Historical analyses** | [Design implications](../../reports/analysis/cwsf2027-design-implications.md), [engineering patterns](../../reports/analysis/engineering-robotics-patterns.md), [AI patterns](../../reports/analysis/ai-project-patterns.md) | Question–comparison–evidence discipline, useful negative results, and student contribution. These do not predict awards. |

**Review limits:** This consolidation reviewed the relevant Markdown plans and source material, not every historical CWSF dataset or every cited paper in full. Abstract-level checks do not establish reproducibility. Older plan language is preserved as history; the October 23 selection supersedes only the earlier uncertainty over the broad topic. Future results should identify their actual evidence type and link to the underlying files.

**Maintenance:** When a decision is made, date it, update the status table, and link the evidence. When an experiment is completed, add its method, version, raw data, analysis, and conclusion; do not convert a planned checkbox or proposed target into a result without that record.

[C1]: #conversation-sources
[C2]: #conversation-sources
[C3]: #conversation-sources
[C4]: #conversation-sources
[C5]: #conversation-sources
[C6]: #conversation-sources
[F1]: https://docs.google.com/document/d/1dZmtxMwA-xtempr4vKt8oG2OuoJ9H_wThzoe6ApOfPU/edit
[F2]: https://docs.google.com/document/d/1LFuOe8CJivYmTWZOr8HUuY-tF338UO4iVYqqSEPBuMM/edit
[D0]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/README.md
[D1]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/01-project-proposal.md
[D2]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/02-physics-and-modeling.md
[D3]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/03-aircraft-and-control-architecture.md
[D4]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/04-experiments-and-evaluation.md
[D5]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/05-roadmap-and-notebook.md
[D6]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/06-annotated-references.md
[D7]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/07-cwsf-story-risks-and-decisions.md
[D8]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/08-thermal-vs-dynamic-soaring.md
[D9]: ../../docs/projects/ai-powered-adaptive-dynamic-soaring/09-sailing-upwind-and-dynamic-soaring.md
[I1]: ../../docs/ideas/adaptive-ai-dynamic-soaring.md
[I2]: ../../docs/ideas/energy-aware-environmental-uav-sensing.md
[I3]: ../../docs/ideas/autonomous-marine-wildlife-uav-monitoring.md
[I4]: ../../docs/ideas/information-foraging-airborne-observatory.md
[I5]: ../../docs/ideas/README.md
[I6]: ../../docs/ideas/bio-inspired-flight-research-options-2026-10-18.md
[P1]: https://doi.org/10.1016/j.pocean.2014.11.002
[P2]: https://doi.org/10.1111/j.1474-919x.2004.00295.x
[P3]: https://doi.org/10.2514/1.43270
[P4]: https://doi.org/10.1016/j.pocean.2016.01.003
[P5]: https://doi.org/10.1186/s40462-018-0121-9
[P6]: https://doi.org/10.1098/rsos.211364
[P7]: https://doi.org/10.1016/j.ifacol.2019.11.079
[P8]: https://doi.org/10.1016/j.dt.2024.12.007
[P9]: https://doi.org/10.1016/j.engappai.2025.111219
[P10]: https://doi.org/10.1016/j.apenergy.2026.127955
[P11]: https://doi.org/10.1038/s41586-018-0533-0
[P12]: https://doi.org/10.1038/s41467-024-48670-x
[P13]: https://arxiv.org/abs/1802.08215
[T1]: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/induced-drag-coefficient/
[T2]: https://ardupilot.org/plane/docs/soaring-4_1.html
[T3]: https://www.flow5.tech/xflr5/xflr5.html
[T4]: https://ocw.mit.edu/courses/3-11-mechanics-of-materials-fall-1999/resources/mit3_11f99_bdisp/
[T5]: https://doi.org/10.1016/j.matdes.2017.03.065
