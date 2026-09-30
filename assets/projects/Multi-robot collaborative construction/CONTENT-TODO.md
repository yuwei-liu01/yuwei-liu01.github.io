# Multi-Robot Collaborative Assembly — content maintenance

This is a team workshop project at Tongji University (2024). Keep the published narrative concise; record unverified details here rather than adding large placeholder panels to the page.

## Confirmed demonstration method

- Three timber overlap action types; each was demonstrated and recorded repeatedly.
- One complete overlap action per video; one video is one trajectory sample. Repeated videos form each action class’s data.
- Board face and direction matter because upper/lower groove orientations differ.
- Eight differently colored semicircular marks near the grooves distinguish feature positions and help observe movement.
- A trajectory follows the same color across time, not a connection between eight marks in one frame. Multiple marks describe translation and rotation together.
- Demonstrations supported machine-learning exploration; performance was limited. Final construction primarily used localization and multi-robot coordination.

## Media needed

- [x] One learning-exploration video below the three action diagrams: `machine-learning.mp4`, supplied by the user. This presentation clip is separate from the repeated-recording dataset.
- [x] Assembly demonstration video: `construction.mp4`, supplied by the user for the page; controls enabled, no autoplay. Detailed video credits remain to be added.
- [ ] One continuous board-handling cycle, or consecutive frames from the same cycle: grip, move to target, release, pick the next board. Do not substitute staged or generated images.
- [ ] Original high-resolution robot-operation photo to replace the current poster excerpt (`robot-operation.jpg`).
- [ ] Environment-localization recording showing the actual workshop setup and visual-marker detection footage.
- [ ] A separate clear final-prototype photograph if available; the current result view is `workshop-prototype.jpg`.

## Technical details to verify

- [ ] Names/definitions of overlap actions A, B and C, and the complete assembly order. These are structural actions, distinct from the four-step board-handling cycle.
- [ ] SLAM implementation, sensing setup, calibration, coordinate frames and transforms. The poster labels describe proposed system design, not proof of each deployed interface.
- [ ] Actual use of AprilTag, Orbbec / RealSense SDKs and UR RTDE; do not infer deployment solely from labels in the retained system overview.
- [ ] Robot roles and coordination procedure beyond the confirmed one localization robot / two assembly robots. Do not infer automatic allocation, collision planning or simultaneous motion.
- [ ] End-effector specifications and camera model. Present the existing exploded view as workshop hardware design.
- [ ] Whether marker trajectories were manually annotated or automatically extracted; tracking code, frame timing, image/world coordinates, occlusion handling and face/direction labeling. Do not infer automated extraction or recovered 3D pose.
- [ ] Any actual training code, model definition, trajectory representation and evaluation records; demonstration videos alone do not establish these.
- [ ] Learning dataset, model and evaluation; performance was limited, and the final construction used localization and coordinated operations. No inferred explanation of the learning limitation.
- [ ] Experimental observations, human involvement, limitations and any measured results. No performance numbers until supporting records exist.

## Credits

- [ ] Official workshop title, team member list, photo/video authors and publication permissions.
- Tutors shown under the project context: Xu Zhen, Zhang Ye, Xiang Wang. Name order reversed at the user’s request from the previous transcription: Zhen Xu, Ye Zhang, Wang Xiang.
- Original poster links removed from the page at the user’s request; source PDF files are retained.
- Personal-contribution section was intentionally removed at the user's request.

## Published image roles

| Section | Asset | Role |
| --- | --- | --- |
| Overview | assembly-overview.jpg | Team setup and reciprocal shell; used once |
| Trajectory Learning Exploration | structure-model.svg | Target structure |
| Trajectory Learning Exploration | assembly-action-a.svg / b.svg / c.svg | Three distinct overlap actions |
| Trajectory Learning Exploration | demonstration-recording.jpg | Team demonstration collection |
| System Overview | Existing system-overview WebP / HD PNG | Unmodified complete functional overview |
| Locate | environment-localization.svg | Redrawn poster concepts |
| Locate | component-markers.jpg | Markers on actual timber |
| Coordinate | workspace-study.svg | Shared-workspace design study |
| Manipulate | end-effector-detail.svg | Gripper, camera and connector design |
| Results | robot-operation.jpg | Existing robot-operation still |
| Results | workshop-prototype.jpg | Physical reciprocal shell in the multi-robot workspace |

The six standalone SVG assets were extracted from the already-approved, self-contained HD system SVG. They reuse its full vector geometry and embedded source-resolution image data, not rendered diagram thumbnails. The original overview and all source files remain unchanged. `extract-story-assets.py` reproduces the extraction beside the source SVG.
