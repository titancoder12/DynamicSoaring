# 09 — Sailing Upwind and Albatross Dynamic Soaring

**Discussion date:** 2026-10-18.  
[Project home](README.md) · [Soaring comparison](08-thermal-vs-dynamic-soaring.md)

## Why can a sailboat head toward the wind?

A sailboat cannot normally sail *directly* into the wind. It heads diagonally upwind, changes tack, then sails diagonally upwind on the opposite tack: **tacking**.

An appropriately trimmed sail acts as a lifting surface. Wind relative to the moving boat (*apparent wind*) produces aerodynamic force with useful forward and sideways components. The keel/hull interacts with water to oppose much of the sideways motion, letting the boat make net progress upwind. The key resource is relative motion of wind and water. It is inaccurate to say wind simply pushes an upwind sailboat from behind.

## Is this the same physics as albatross dynamic soaring?

**Similar principle, different mechanism.** Both exploit relative motion between media or moving air masses to obtain useful energy and travel upwind without continuous onboard propulsion.

| | Sailboat | Dynamic-soaring albatross |
|---|---|---|
| Different velocities | Air vs water | Faster vs slower *air layers* |
| Aerodynamic surface | Sail | Wings |
| Interaction | Continuous aerodynamic lift plus hydrodynamic keel/hull forces | Sequenced flight maneuvers crossing wind-shear layers |
| Upwind travel | Alternating tacks | Repeated appropriately oriented climbs/turns/descents |
| Critical physics | Apparent wind, lift, hydrodynamic side force | Wind gradient, airspeed changes, drag and energy accounting |
| Important limit | Cannot generally point straight into wind | Uniform steady wind cannot power a sustained closed unpowered soaring cycle |

A sailboat engages wind and water *simultaneously*. An albatross interacts with local air at each moment; its trajectory traverses layers moving at different velocities. Aircraft inertia enables useful changes in air-relative speed as the bird crosses a shear layer. Calling it an “invisible keel” is **only an analogy**, not a literal keel or hydrodynamic force.

## Connection to our CWSF project

This motivates a precise engineering question: can onboard estimation + adaptive control identify where the aircraft can extract energy from wind shear and choose a safe maneuver? Compare energy gained against drag losses and propulsion energy; distinguish net useful mission energy from instantaneous airspeed or ground-speed changes.

Possible extension: optimized **upwind survey routes** using dynamic soaring (if the airframe and wind support it); treat Richardson's idealized two-layer predictions as model-specific upper bounds, not attainable FW-01 speeds.

## Research papers

1. **Richardson, P. L. (2015).** *Upwind dynamic soaring of albatrosses and UAVs.* Progress in Oceanography 130, 146–156. https://doi.org/10.1016/j.pocean.2014.11.002 — specifically analyzes upwind maneuvers and a robotic-albatross UAV; closest paper to the sailboat/tacking discussion.
2. **Richardson, P. L. (2011).** *How do albatrosses fly around the world without flapping their wings?* Progress in Oceanography 88, 46–58. https://www2.whoi.edu/staff/prichardson/publications/ — foundational oceanic flight discussion and author-hosted reading links.
3. **Sachs, G. (2005).** *Minimum shear wind strength required for dynamic soaring of albatrosses.* Ibis 147, 1–10. https://doi.org/10.1111/j.1474-919x.2004.00295.x
4. **Deittert, M. et al. (2009).** *Engineless unmanned aerial vehicle propulsion by dynamic soaring.* Journal of Guidance, Control, and Dynamics 32, 1446–1457. https://doi.org/10.2514/1.43270
5. **Richardson, Wakefield & Phillips (2018).** *Flight speed and performance of the wandering albatross with respect to the wind.* Movement Ecology 6. https://doi.org/10.1186/s40462-018-0121-9
6. **Richardson & Wakefield (2022).** *Observations and models of across-wind flight speed of the wandering albatross.* Royal Society Open Science 9, 211364. https://doi.org/10.1098/rsos.211364

**Caution:** the sailing analogy is useful for intuition, not a substitute for a correctly framed aerodynamic and inertial energy-balance derivation.
