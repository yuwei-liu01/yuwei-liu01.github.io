# Haptic project assets

- `system-photo.jpg`: extracted from final report Fig. 1; resized to 1600 × 1200 for the web. Retained as an original prototype reference.
- `simulation-contact-proxy.png`: original embedded image from final report Fig. 3.
- `system-architecture.svg`: editable vector adaptation of the supplied `haptic-force-cepx-architecture.png` and report architecture. The supplied workspace/repository contained no original SVG. Adds explicit ESP32-C6 identification and separates the forward and feedback paths.
- `force-command.svg`: original embedded Fig. 4 pixels in an SVG, with only the legend and right-axis label replaced. Curves, tick values, and left-axis force units are unchanged. The report's “Torque (Nm)” label is not treated as verified calibration or measured torque. Right-axis units need confirmation.
- `final-report.pdf`: unchanged supplied final report. Its original terminology is retained in the source document; the web presentation clarifies the command/measurement distinction.

## Publication status

All media used on the current page is present: animated cover and poster, trimmed demonstration and poster, simulation image, architecture diagram, hardware diagram, result plot, and final report. Snapshot, contribution/team, and Resources sections were removed at the owner's request; do not restore their old placeholders. Motor-command units remain unverified and are explicitly qualified on the page. The CAD study is explanatory rather than a manufacturing assembly drawing.

## Cover and demonstration

- `cover.mp4` and `cover.png`: approved v4 CAD/screenshot composition with corrected fixed ring, matching gray background, scaled CAD and central signal arrows. The right-side animation is illustrative, not newly computed SOFA output. The page uses `cover.gif` for reliable animated display without video decoding; MP4 is retained as an alternate export. The PNG is the portfolio card cover.
- `demo.mp4`: supplied `HapticForceCepxDemo.MOV`, trimmed from 16.600 seconds to the end (about 7.63 seconds), re-encoded to H.264/AAC for browser playback. First audio stream retained; playback defaults to muted. Original MOV is unchanged.
- `demo-poster.jpg`: first frame of the trimmed demonstration.
- Both videos use autoplay, muted, loop, playsinline, controls, and responsive dimensions.

The project source repository remains private. Do not add a public source link without updated instructions.

## Hardware analysis figure

`hardware-analysis.svg` and `hardware-analysis.png` use real STEP geometry from the supplied STEP Files.zip and LILYGO's `3D_File/H718-20240809.stp`, pinned to commit a7d9189e4099875dff4a1a7dad4b07257b1ff508. This is a separated component study, not a verified assembled model. Relative scale is preserved; displayed positions and rotations are explanatory. The finger ring is shown once, with quantity and placement unconfirmed. Vendor cable solids are omitted. Controller, driver, and encoder identities come from the vendor README; individual chip locations are not inferred from the generic CAD solids. No public project source-repository link is added; the external link is the vendor hardware source.

The detail page uses `cover-wide.gif`, cropped from the v4 GIF (1008 × 560 to 1008 × 314, removing vertical background margins). All geometry and signal arrows are retained. The recorded demonstration follows the cover directly, before section navigation and content cards.

The page now uses `demo-silent.mp4`, a video-only remux with the audio track removed so sound cannot be enabled. The original recording remains unchanged. The visible report link was removed at the owner’s request.

`system-architecture.png`: supplied original PNG, now used on the page at the owner’s request. Report supports the hardware, two-loop rates, local model, LCP contact processing, serial protocol and nonlinear command mapping. “Stable local feedback” describes the design intent, not independently verified stability; torque labels represent commanded output, not measured torque. Contact-loss decay applies to K, with B set to zero in the report algorithm.
