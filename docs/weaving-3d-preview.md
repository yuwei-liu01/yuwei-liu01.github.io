# 3D kinematic preview

Local static Canvas renderer with a 3D orbit camera, geometric IK and no external libraries. It animates the approved Pattern III sequence only. Existing 2D players are unchanged.

## Source audit
Read 0711/roboticArm.3dm using rhino3dm. Units: millimeters; 237 objects. Layers include 00-ref-L, 01-moto, 02-mental structure, 03-bolts. The 00-ref-L reference lines include a coherent skeleton at x=0: z=0 to85; z=85 to192 (107); (y=-683.251,z=192) to(y=-518.706,z=287), length190; and the following 50 mm segment. These reference lengths inform the simplified arm. Also read 0831/IK模型最终调试0831.3dm (315 objects, mm). GH definition contains geometric and ordering components but has not been executed here.

## Assumptions
This is not a mesh export or full six-axis digital twin. Actual metal parts, motor offsets, joint limits and TCP calibration are not yet mapped to a rig. Renderer uses base yaw, shoulder/elbow planar IK and wrist pitch to maintain a vertical tool. The 50 mm reference segment is used as an illustrative tool offset, not a verified needle TCP. Frame 95×110 mm at (190,-55,18), orientation and timing are illustrative. Path is the current user-approved normalized Pattern III sequence. No lifts or wraps added. Lines visualize laid thread, not material mechanics or collision simulation.

## Files
assets/projects/robotic-weaving/preview-3d/model.json: dimensions and placement.
kinematics.js: IK and path mapping.
viewer.js: camera, canvas drawing, playback and controls.
projects/desktop-robotic-arm.html and robotic-weaving.css: embedded accessible controls and responsive panel.

Next data required: verified joint axes/limits and per-link mesh grouping; frame/base transform; needle TCP offset and orientation; full poses for approach/withdrawal and anchor wrapping.

Validation: sampled 101 positions on each of 13 path segments (1,313 total); all reachable in this mathematical model. Forward-kinematic TCP residual below 1e-10 model units (numerical consistency only, not physical accuracy). Browser play/pause, progress-to-end, reset, speed selection and reference toggle checked; error log empty. 390 px viewport has no horizontal overflow. No deployment performed.
