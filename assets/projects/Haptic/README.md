# Haptic project assets

- `system-photo.jpg`: extracted from final report Fig. 1; resized to 1600 × 1200 for the web. Used as hero and portfolio card cover.
- `simulation-contact-proxy.png`: original embedded image from final report Fig. 3.
- `system-architecture.svg`: editable vector adaptation of the supplied `haptic-force-cepx-architecture.png` and report architecture. The supplied workspace/repository contained no original SVG. Adds explicit ESP32-C6 identification and separates the forward and feedback paths.
- `force-command.svg`: original embedded Fig. 4 pixels in an SVG, with only the legend and right-axis label replaced. Curves, tick values, and left-axis force units are unchanged. The report's “Torque (Nm)” label is not treated as verified calibration or measured torque. Right-axis units need confirmation.
- `final-report.pdf`: unchanged supplied final report. Its original terminology is retained in the source document; the web presentation clarifies the command/measurement distinction.

## Assets and details still needed

- Approved 15–30 second MP4 demo. `HapticForceCepxDemo.MOV` exists in the parent workspace but is intentionally not published or substituted for the requested placeholder.
- Annotated hardware photograph or CAD figure.
- Yuwei Liu's role and individual technical contributions.
- Timeline, course, semester, advisor, and award/recognition (or confirmation of none).
- Confirmed motor-command units/calibration; raw plotting data if available.

## Adding the demo

In `projects/haptic-force-cepx.html`, replace `.demo-placeholder` with the video inside `#demo-video-template`, set the source `src` to the approved MP4 in this directory, and remove the template. Keep `autoplay muted loop playsinline controls` and `type="video/mp4"`; `.haptic-video` already supplies responsive styling. Until then the template makes no missing-file request.

The project source repository remains private. Do not add a public source link without updated instructions.
