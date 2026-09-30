# Project material sources

## Localization camera illustration (2026-09-30)

- `localization-camera-view.png` is the complete first and only page of `OP5-digital futures/process/三哥相机视角_复制.pdf`, rendered at 2400 × 1204 pixels with Poppler (`pdftoppm -scale-to 2400 -singlefile -png`). The source PDF is preserved in the project material folder.
- This is a workshop technical illustration of the camera viewpoint, not a recorded camera frame. All trajectory lines, axes, arrows and labels were already in the source; no overlays, detection results or performance claims were added. No cropping or stretching was applied.
- Displayed below the environment-localization diagram and component-marker photograph, with a full-size image link.

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

## Five-part narrative revision

Six standalone SVGs reuse complete nested assets from the approved `system-overview-hd.svg`: `structure-model.svg` (nested SVG 0), `assembly-action-a.svg` / `assembly-action-b.svg` / `assembly-action-c.svg` (1–3), `workspace-study.svg` (4), and `end-effector-detail.svg` (13). Indices are zero-based among nested SVG elements. All local clip definitions and original embedded image data are retained. Only the outer placement and display dimensions are removed; viewBox geometry is preserved. `extract-story-assets.py` reproduces them.

The HD overview is unchanged. Existing white-background crops/masks avoid screenshot borders; technical drawings are displayed on white in both themes. No new experimental imagery or action labels were generated. See `CONTENT-TODO.md` for missing footage and technical details.

## User-supplied videos (2026-09-29)

Source folder: `OP5-digital futures/video/`. Original MOV files remain there unchanged.

- `construction.mp4` ← `video/construction.mov` (126.47 s, HEVC 3436 × 1932); placed at `#assembly-demo`.
- `machine-learning.mp4` ← `video/machine learning.MOV` (7.80 s, HEVC 3840 × 2160 with AAC audio); placed at `#learning-demo`.
- Web copies: H.264, 1920 × 1080, yuv420p, original timing, MP4 faststart. Existing audio preserved as AAC; no autoplay.
- `construction-poster.jpg`: actual construction video frame at 10 s.
- `machine-learning-poster.jpg`: actual learning video frame at 2 s. This is a workshop presentation clip, not a claim of trained-model deployment.
- Encoding: FFmpeg scale `1920:-2:flags=lanczos`, libx264 medium, CRF 23 (construction) / 22 (learning), AAC 128k where present, `-movflags +faststart -map_metadata -1`.
