# Robotic Weaving — System Overview

This revision changes only the weaving project's system diagram and its embedding. The multi-robot project is unchanged. Earlier weaving page, card and animation work remains in this local checkout.

## Deliverables
- `assets/projects/robotic-weaving/system-overview.svg`: editable text, module backgrounds and connectors; simplified workflow per the October 2 reference.
- `assets/projects/robotic-weaving/system-overview-mobile.svg`: vertical workflow version preserving both inputs and the hardware-support branch.
- `assets/projects/robotic-weaving/system-overview.png`: 4800 × 1740 preview.
- `tools/build-weaving-overview.py`: reproducible layout/export, using Python Pillow, PyGObject, Cairo and librsvg.
- `projects/desktop-robotic-arm.html` and `projects/robotic-weaving.css`: responsive picture, full-size link and download links. Justified body text retained.

## Original materials
- Pattern I / II / III: existing independent renders of 素材/M2.pdf, M3.pdf, M1.pdf respectively.
- Grasshopper definition and coordinate panel: 素材/gh.png; derived copies in `system-sources/`.
- A/B ordering rule and serial transmission: extracted original Grasshopper Python sources already preserved as `grasshopper-ordering-source.py` and `grasshopper-serial-source.py`.
- Robot model, frames, target and geometric IK: existing independent crops from Portfolio_Yuwei_Liu.pdf, page 4 (`tool-frame.jpg`, `base-frame.jpg`, `tcp-target.jpg`, `ik-circles.jpg`, `joint-angles.jpg`).
- Controller board: 素材/DLB.pdf (`control-board.jpg`).
- Threading tool: 素材/endeffector1.pdf (`threading-tool.jpg`).
- Servo wiring and physical tests: existing `servo-wiring.jpg`, `execution-middle.jpg`, `woven-frame.jpg` from original project photographs.

## Evidence and open questions
The original A/B rule is a general list-ordering script, not a verified complete execution program for each pattern. The displayed coordinate panel is a source screenshot, not a newly inferred anchor table. Need per-pattern evaluated anchor IDs, ordered TCP poses, tool orientation and units, plus matching command exports, to establish complete original execution order.

Geometric inverse-kinematics diagrams and Grasshopper definitions support the IK label. Complete six-axis solution coverage, singularity handling and accuracy are unverified. No such performance claims are made.

The diagram distinguishes final thread connections from tool movement. No lifting, lowering, anchor wrapping, collision checks or feedback loop is invented. Photos establish a square-frame test, not physical validation of all three patterns. Serial communication precedes the controller and servo signals; no unverified PWM, torque or supply figures are copied.

The October 2 revision uses two preparation routes matching the new user reference. Ordered TCP targets and the kinematic model feed joint-angle calculation, which outputs joint commands to control. Servo initialization has a dashed support connection directly to control, never to the command calculation. Execution observations are terminal; no feedback loop is implied. The control box explicitly distinguishes computer serial commands from controller servo signals. The workflow omits photographs by request; original imagery and source assets remain preserved elsewhere on the project page and on disk.

## Validation
Desktop 1280 px and mobile 390 px: diagram loaded, no horizontal page overflow. Mobile selects the stacked SVG. Browser warning/error log empty after reload. All images are embedded in the SVGs; PNG and SVG links resolve to local files. SVGs parsed successfully; export rendered with librsvg. `git diff --check` passed. Multi-robot HTML SHA-256 unchanged: aed158dfb2a2a8d90813eb340c193607c0e7a909326283cc0db1def9c6943e75.

Local preview only; no push or deployment.

October 2 update: regenerated desktop/mobile SVG and 4800 × 1740 PNG; updated figure alt text and caption. Inspected desktop rendering and checked SVG structure and whitespace. No animation or other project files changed in this revision.

The diagram-only revision removes all visible top headings and bottom workflow-summary text from both SVGs and crops their canvases to the workflow. Original module labels and connections are unchanged. Unverified execution-order details remain documented here.
