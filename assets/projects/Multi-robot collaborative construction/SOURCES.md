# Project material sources

Original files are preserved. Images are resized proportionally; only named board excerpts are cropped. No generated images are used.

- `assembly-overview.jpg` ← `Existing repository cover.png`
- `workshop-prototype.jpg` ← `素材/2.png`
- `component-markers.jpg` ← `素材/顶视图/图1_new-24.jpg`
- `demonstration-recording.jpg` ← `素材/jxxxzp/17.jpg`
- `physical-test.jpg` ← `素材/gccc/图1_new-9.jpg`
- `prototype-detail.jpg` ← `素材/展示/5.jpg`
- `parametric-design.jpg` ← `board1 PDF, crop coordinates at 1080 × 1800: (323, 473, 1047, 637)`
- `component-design.jpg` ← `board1 PDF, crop coordinates at 1080 × 1800: (30, 473, 313, 793)`
- `assembly-study.jpg` ← `board1 PDF, crop coordinates at 1080 × 1800: (322, 987, 1047, 1254)`
- `environment-localization.jpg` ← `board2 PDF, crop coordinates at 1080 × 1800: (718, 163, 1046, 331)`
- `workshop-board-1.pdf` ← `图1_new.pdf`
- `workshop-board-2.pdf` ← `图2_new.pdf`

board1 = 图1_new.pdf; board2 = 图2_new.pdf. Local source folder: OP5-digital futures.

Tutors verified visually on both PDF headers: Zhen Xu (许蓁), Ye Zhang (张烨), Wang Xiang (王祥). Student list has inconsistent romanization; full team credits await confirmation. No playable video was found in the repository or supplied material folder. The original boards include exploratory approaches; these are not evidence of successful deployment.

## Robotics-focused revision

- `robot-operation.jpg`: photograph excerpt from board 2, crop (748, 667, 1044, 862) at 1080 × 1800 reference size. Shows a single robot-operation scene, not a verified temporal sequence.
- `end-effector-study.jpg`: labeled hardware drawing excerpt from board 2, crop (479, 648, 742, 865) at 1080 × 1800 reference size. The source explicitly labels Metal Grab, Metal Connector, Orbbec Camera, and 3D Printing camera holder. This is a drawing, not a hardware photograph.
- Page organization references https://fabrica.csail.mit.edu/ (reviewed 2026-09-27); no imagery, research claims, algorithms, or results from that project are reused.
- No verified consecutive robot-action frames were found. Three clearly labeled placeholders reserve this sequence rather than presenting manual demonstrations as robotic execution.

## Illustrated system overview

`system-overview.svg` and `system-overview-mobile.svg` are self-contained vector layouts with embedded copies of the existing project images: parametric-design.jpg, component-design.jpg (desktop), assembly-study.jpg, environment-localization.jpg, component-markers.jpg, robot-operation.jpg, and assembly-overview.jpg. No external project imagery is included. Arrows represent only the confirmed functional relationships. The mobile layout reflows these relationships; it does not represent a different system.

## Approved HD overview integrated into project page

- `system-overview-hd.svg` and `system-overview-hd.png` reproduce the final artifact in OP5-digital futures/output/system-overview-hd, with the straight sequence arrow and removed header/footer text.
- `system-overview-web-1200.webp` and `system-overview-web-2400.webp` are proportional web previews generated from the 6000 × 3400 PNG; no diagram content was changed.
- The page uses the same approved three-column diagram on desktop and mobile; the mobile view supports horizontal scrolling and an original-resolution link. Older system-overview.svg/system-overview-mobile.svg are retained as unreferenced prior assets.
- Missing video, localization visualization and consecutive operation frames remain labeled placeholders.

## Environment-localization vector redraw

- `environment-localization.svg` replaces the screenshot crop in the Environment Localization section. All icons, arrows and text are native SVG; no raster images or third-party icons are embedded.
- Source: the workshop diagram supplied as `codex-clipboard-d534a806-df97-4609-b9ce-ace355c9fab3.png`, corresponding to the environment/mapping area of workshop board 2. The mapping branch and spatial-planning branch are redrawn; learning, camera SDKs, manipulation and fabrication branches are outside this section.
- Labels such as RViz, electronic fence and path planning reflect the source diagram, not independently verified implementation or performance. The caption states this boundary; the recorded-localization placeholder remains.
- `build_environment_diagram.py` regenerates the standalone SVG using the Python standard library. The original `environment-localization.jpg` is preserved.

- Deployment preparation: one embedded PNG stream in `system-overview-hd.svg` was losslessly re-encoded after GitHub mistook compressed image data for an access token. The source PNG contained only IHDR, pHYs, IDAT and IEND chunks, with no textual metadata. Decoded RGB pixels were verified identical; diagram text and vector paths are unchanged.
