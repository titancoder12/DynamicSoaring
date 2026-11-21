# Bio-inspired Flight Engineering Options — CWSF 2027

**Discussion date:** 2026-10-18. **Status:** eight candidate directions plus flying seeds, none selected or experimentally demonstrated.  
[Main dynamic-soaring project dossier](../projects/ai-powered-adaptive-dynamic-soaring/README.md)

## Idea catalogue and student engineering experiments

| Inspiration | Mechanism | Candidate project | Measurable outcomes |
|---|---|---|---|
| Eagles / vultures | Circle within rising thermals | AI thermal detection and centering | Climb rate, acquired lift, endurance, acquisition time |
| Swifts | Change wing sweep / geometry | AI-controlled morphing wing | Glide/sink rate, lift-to-drag, turn rate, actuator energy |
| Owls | Serrated leading edges and surface texture | Quiet UAV wing-edge variants | Sound spectrum, lift/drag, stall margin |
| Hawks | Separated primary-feather wingtip slots | 3D-printed slotted/adaptive wingtips | Induced drag proxy, glide ratio, turn efficiency |
| Dragonflies | Corrugated small-scale wings | Corrugated vs smooth airfoil | Lift/drag and flow robustness at matched Reynolds number |
| Humpback whales | Leading-edge tubercles on flippers | Tubercled vs smooth UAV wing | Stall onset, maximum lift, drag tradeoff |
| Bees | Optic-flow vision for navigation/approach | Camera-aided fixed-wing landing | Approach error, lighting robustness, GPS-denied performance |
| Frigatebirds | Thermals, atmospheric convection, weather-sensitive routing | Energy-aware atmospheric navigation | Total energy, mission distance and survival under uncertainty |
| Maple / dandelion seeds | Passive autorotation / porous vortex-supported descent | Low-cost atmospheric sensor gliders/descenders | Descent rate, dispersion, payload data, recovery and footprint |

**Implementation note:** the FW-01 flying wing, if measured and safe, is relevant to ideas involving fixed-wing flight control, morphing, aerodynamic surfaces and wind sensing. Some concepts require a different airframe. Do not assume biological aerodynamic effects scale automatically to 85 cm wings or aircraft Reynolds numbers.

## Discussion recommendation

- **Swift morphing wings:** strongest visibly mechanical build; experimentally isolate geometry and actuator trade-offs.
- **Eagle/vulture thermal soaring:** strongest near-term outdoor autonomy/flight demonstration using existing ArduPilot/ArduSoar systems.
- **Frigatebird navigation:** environmental energy routing with atmospheric sensing, potentially a later extension.
- **Albatross dynamic soaring:** more advanced shear-based trajectory and flight-energy physics with a higher outdoor validation barrier.
- **Owl / hawk / dragonfly / whale:** excellent controlled aerodynamic design experiments without requiring full autonomy.
- **Optic flow / flying seeds:** alternative flight applications with distinctive hardware.

These are qualitative strategy views, **not** CWSF medal forecasts. Project merit depends on measured evidence and student contribution. The student's preferred approach is **Build → Understand → Reproduce → Experiment → Improve**, using professional work as a foundation rather than abandoning an idea simply because scientists studied it first.

## Verified primary literature and experimental starting points

1. **Lentink et al. (2007).** *How swifts control their glide performance with morphing wings.* Nature 446, 1082–1085. https://doi.org/10.1038/nature05733 — wind-tunnel measurements of swift wings and sweep tradeoffs.
2. **Jeger et al. (2024).** *Adaptive morphing of wing and tail for stable, resilient, and energy-efficient flight of avian-inspired drones.* npj Robotics 2, 8. https://doi.org/10.1038/s44182-024-00015-y — flown LisEagle prototype, controller, energy optimization, linked data/code.
3. **Reddy et al. (2018).** *Glider soaring via reinforcement learning in the field.* Nature 562, 236–239. https://doi.org/10.1038/s41586-018-0533-0 — real thermal-soaring glider.
4. **Flato et al. (2024).** *Revealing principles of autonomous thermal soaring in windy conditions using vulture-inspired deep reinforcement-learning.* Nature Communications 15, 4942. https://doi.org/10.1038/s41467-024-48670-x.
5. **Tabor et al. (2018).** *ArduSoar: an Open-Source Thermalling Controller for Resource-Constrained Autopilots.* https://arxiv.org/abs/1802.08215.
6. **Tucker (1995).** *Drag reduction by wing tip slots in a gliding Harris' hawk.* Journal of Experimental Biology 198, 775–781. https://doi.org/10.1242/jeb.198.3.775.
7. **Miklosovic et al. (2004).** *Leading-edge tubercles delay stall on humpback whale flippers.* Physics of Fluids 16, L39–L42. https://doi.org/10.1063/1.1688341.
8. **Biradar et al. (2024).** *Bio-inspired corrugated airfoil aerodynamics under external turbulence at low Reynolds numbers.* Journal of Flow Visualization and Image Processing 31, 75–97. https://doi.org/10.1615/JFlowVisImageProc.2023049120.
9. **Owl-inspired leading-edge serrations play a crucial role in aerodynamic force production and sound suppression (2017).** Bioinspiration & Biomimetics. https://doi.org/10.1088/1748-3190/aa7013.
10. **Weimerskirch et al. (2016).** *Frigate birds track atmospheric conditions over months-long transoceanic flights.* Science 353, 74–78. https://doi.org/10.1126/science.aaf4374.
11. **Cummins et al. (2018).** *A separated vortex ring underlies the flight of the dandelion.* Nature 562, 414–418. https://doi.org/10.1038/s41586-018-0604-2.
12. **Richardson (2015).** *Upwind dynamic soaring of albatrosses and UAVs.* Progress in Oceanography. https://doi.org/10.1016/j.pocean.2014.11.002.

**Unverified details:** We discussed bees' optic-flow landing and maple-seed autorotation, but no specific matching primary paper was verified during this update; do not attribute these ideas to a fabricated citation. The overall concepts remain valid research leads, pending targeted literature searches.

## Connections to other repo ideas

- [Standalone AI adaptive control](adaptive-fixed-wing-flight-control.md)
- [Standalone albatross dynamic soaring](bio-inspired-dynamic-soaring.md)
- [Combined AI + dynamic soaring](adaptive-ai-dynamic-soaring.md)
- [Separate cooperative thermal soaring](cooperative-thermal-soaring-search.md)
- [Separate 1+3 fixed-wing swarm](wind-adaptive-decentralized-fixed-wing-swarms.md)

All performance claims from external studies are **their** reported results under their conditions, not validated gains for FW-01.
