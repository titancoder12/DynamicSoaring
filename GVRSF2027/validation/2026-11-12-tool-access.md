# Tool and repository access — 2026-11-12

Working directory: `/workspace/scratch/5aeb3b0e05c5/cwsf2027-research` (cloud Linux).

| Check actually performed | Result |
| --- | --- |
| GitHub repository metadata | Private `eugenelin89/cwsf2027-research`; read/write permission available through the connected GitHub tools. |
| Remote `main` | `e12f10327d36210981db4b19d82fa0637ab229f4`; branch metadata reports `protected: false`. |
| Existing cloud checkout | Found an older, clean snapshot at `/workspace/scratch/7683ac43298e/cwsf2027-research`, ending at `60567d5`; it had no configured remote. Left untouched. |
| Ordinary Git HTTPS | `git ls-remote` failed because no Git CLI credentials are configured. No credentials were extracted or copied. |
| Working-copy method | Required source files fetched through GitHub at the exact baseline into a fresh scoped working copy. This is not a full clone. Remote commits will preserve the complete baseline tree and change only an explicit manifest. |
| Native Blender executable | Cloud `/usr/bin/blender`, 4.3.2, successfully ran `--version`. |
| Solid CAD imports | CadQuery 2.7.0, build123d 0.10.0, OCP 7.8.1.1 imported successfully. CadQuery selected to preserve editable Python and genuine STEP solids. |
| Other CAD | OpenSCAD executable found, not selected or executed for this model. |
| Slicer executable discovery | Bambu Studio / PrusaSlicer not found on PATH. No slice or configured slicer project claimed. |
| User's computer | No Mac filesystem, native-app or remote-shell connection exposed to this session. The available cloud Blender is not the user's installation. Mac Blender and Bambu Studio version/access remain unverified. |

Normal fast-forward GitHub Git Data updates with expected-head checks are used for publication; no force updates. Each milestone will be read back remotely and checked against uploaded file hashes. Dependencies, temporary render files and unrelated historical data are excluded.
