# Robotic weaving: source audit and implementation notes

Local work only; no push or deployment. Repository: `yuwei-liu01/yuwei-liu01.github.io`.
Baseline commit: `0ba35d7`. Work is in the separate `site-local` checkout under the original OP2 source directory. The existing checkout at `/home/itsvera/yuwei-liu01.github.io` was not altered.

## File changes

Modified existing files:

- `index.html` — project card title and summary; original link retained.
- `projects.html` — same card update for All Projects.
- `projects/desktop-robotic-arm.html` — five-section technical project page.

Added implementation and documentation:

- `projects/robotic-weaving.css` — scoped layout and responsive styles.
- `assets/projects/robotic-weaving/toolpaths.json` — separate geometry and movement records.
- `assets/projects/robotic-weaving/toolpath-player.js` — dependency-free SVG player.
- `tools/extract-weaving-data.py` — reproducible PDF vector extraction.
- `docs/robotic-weaving-development.md` — provenance and reconstruction assumptions.
- `docs/robotic-weaving-validation.md` — local checks and limitations.
- The 17 JPG derivatives and two extracted source scripts listed in the media table below.

## Correct page and metadata

The project maps to `projects/desktop-robotic-arm.html` (existing homepage and All Projects links), not `multi-robot-construction.html`. The old website page was a generic assembly placeholder. Identity and metadata were confirmed against `Portfolio_Yuwei_Liu.pdf`, PDF pages 3–7, in the user's `申请文件/00 基础文件（cv，por，cer）` directory:

- Original title: Robotic Rhythms of the Traditional Yurt.
- Date: Fall 2024.
- Instructor: TENG TENG.
- Individual project. No team-project metadata is reused.

The original site links, source models, InDesign document and all source media are preserved. Original material lives outside the website checkout and is not copied wholesale into it.

## Inspected evidence

- `project-robotic.indd`: source layout located; not edited.
- `0705/机械臂.gh`, `0705/建模.3dm`: early files located.
- `0711/IK模型最终调试0721.gh`, `0711/IK模型最终调试参考.gh`, `0711/toolpath auto update python.gh`: GH binary archives decompressed with raw DEFLATE for inspection.
- `0831/IK模型最终调试0831.gh`: inspected component descriptions and extracted four unique Python scripts. Found curve intersection, projection and vector-angle components, two serial-port script variants, an update counter, and alternating point-list ordering. No claim is made that this inspection evaluates the entire definition or proves six-axis IK coverage.
- `0831/亭子.gh`: archive inspected for point-ordering code; no building material is used on the page.
- Rhino files including `0711/roboticArm-0917.3dm`, `0711/IK模型最终调试0721.3dm`, and `0831/IK模型最终调试0831.3dm` are present. Rhino/Grasshopper was not executed in this Linux preview environment; referenced geometry, calibration, and evaluated outputs were not recovered as a complete executable route.
- `0831/weaving.pdf` page 2 gives partial anchor-order examples. These refer to earlier studies and are not assumed to be complete programs for the final three patterns.
- `0707/ROBOIDE/Arduino程序.ino` is a board/serial demonstration, not a three-pattern robot program. Its serial settings differ from the GH source. It is not presented as the computer's production program.
- No standalone, complete export linking each of I/II/III to ordered calibrated TCP poses and corresponding joint/servo commands was found in the inspected files. A few command strings printed on the poster do not establish that mapping.

## Media used

All website outputs below are under `assets/projects/robotic-weaving/`.

| Website asset | Original source | Processing |
| --- | --- | --- |
| `pattern-I.jpg` | `素材/M2.pdf` | Render independent vector drawing; trim whitespace; increase line contrast |
| `pattern-II.jpg` | `素材/M3.pdf` | Render independent vector drawing; rotate 90° clockwise to match poster II; trim whitespace; increase contrast |
| `pattern-III.jpg` | `素材/M1.pdf` | Render independent vector drawing; trim whitespace; increase contrast |
| `base-frame.jpg`, `tool-frame.jpg`, `tcp-target.jpg`, `ik-circles.jpg`, `joint-angles.jpg`, `kinematic-links.jpg` | `Portfolio_Yuwei_Liu.pdf`, PDF page 4 | Crop individual annotated technical diagrams from a 3000px render; retain labels; no entire poster embedded |
| `arm-exploded.jpg` | `素材/bzt.pdf` | Independent exploded drawing rendered and trimmed |
| `threading-tool.jpg` | `素材/endeffector1.pdf` | Independent threading-needle drawing rendered and trimmed |
| `servo-wiring.jpg` | `素材/zp/13.jpg` | Original board/servo wiring photograph, downscaled proportionally |
| `execution-start.jpg` | `素材/zp/1.jpg` | Original early-stage photo |
| `execution-middle.jpg` | `素材/zp/4.jpg` | Original intermediate-stage photo |
| `execution-late.jpg` | `素材/zp/8.jpg` | Original later-stage photo |
| `woven-frame.jpg` | `素材/zp/12.jpg` | Original single-frame result photo |
| `control-board.jpg` | `素材/DLB.pdf` | Independent board drawing retained as an additional extracted asset; page uses the wiring photograph |
| `grasshopper-serial-source.py` | First `CodeInput` in `0831/IK模型最终调试0831.gh` | Extracted source with provenance comment; Python 2 / .NET context, not browser code |
| `grasshopper-ordering-source.py` | Alternating point-list `CodeInput` in same GH file | Extracted source with provenance comment |

Line contrast is adjusted only in derived pattern images; no source PDF or photograph is overwritten. No fabricated imagery is used. The website keeps each image's proportions.

The original PWM panel on portfolio page 5 was checked: it mixes milliseconds with reciprocal-second expressions (e.g. the printed 1 ms versus 1/2500 s), does not establish a consistent waveform period, and uses mass-like labels for torque. This cannot substantiate pulse ranges, frequency, power, or torque specifications. These numbers and the ambiguous waveform panel are omitted. The new control flow distinguishes computer serial strings from control-board servo signals.

## Geometry and reconstruction assumptions

`toolpaths.json` is deliberately separate from `toolpath-player.js`. It contains frame vertices, named anchors, reference chord pairs, and explicit `weave`/`travel` movement records. Positions are dimensionless SVG drawing coordinates, not millimeters or calibrated robot poses. Anchor names `A01` etc. are new visualization identifiers, not original GH branch indices.

`tools/extract-weaving-data.py` reads the actual painted PDF straight-line operators with their affine transformations using pypdf. It discards page/crop marks, duplicates, and same-edge boundary strokes. It retains interior thread connections with endpoints on the frame. The retained frame strokes are displayed separately as the boundary.

| Pattern | Source mapping confirmed on portfolio page 6 | Interior thread connections | Visualization steps |
| --- | --- | ---: | ---: |
| I | `M2.pdf`: triangle, base-to-sloping-edge fans | 18 | 35 |
| II | `M3.pdf`: two fans forming an open arch after rotation | 18 | 35 |
| III | `M1.pdf`: overlapping connections across four edges | 64 | 127 |

- I keeps the triangular drawing's proportions. II/III normalize the original rectangular drawing bounds to a square display frame; endpoint relationships and relative position along each edge are retained. This normalization is not a dimensional measurement.
- The order of painted interior chords in each PDF is retained for reproducibility only. **PDF paint order is not established robot execution order.** The source GH alternating A/B list script is provided as evidence, but its evaluated inputs have not been unambiguously mapped to all three final drawings.
- Between successive disconnected chords, a straight dashed reposition is inserted. It deposits no thread in the visualization. Actual edge-following thread, continuity between winding passes, starting points, group order, and tie-off locations are not established. No 3D lift, lowering, anchor loop radius, orientation interpolation, or tension behavior is invented.
- Reference lines are faint gray; completed threads remain solid teal; the current tool point is orange; the target ring and arrow are purple. Travel moves are dashed and never enter the persistent thread pattern.
- All panels use the same normalized 35-second presentation timeline at 1×. The speed multiplier changes viewing time, not robot feedrate; segments have equal display duration within a pattern. Synchronized play restarts all three at zero. This is not physical simulation, collision checking, or machine validation.
- The UI explicitly labels the result “Reconstructed toolpath visualization.” Photographs support a square-frame weaving test, not execution of all three patterns.

## Data still needed for a faithful execution replay

1. Evaluated per-pattern anchor IDs and complete visit sequences, including start/end, boundary runs and transitions between connection families.
2. Ordered TCP position and orientation exports with units, base/workpiece coordinate frames, and transforms.
3. Verified tool offset and anchor geometry; lift/lower distances and approach/exit/wrapping paths, if used.
4. Corresponding joint-angle/servo-command logs, axis-channel mapping, limits and calibration, plus timing.
5. Clearly labeled execution records identifying which of I/II/III was run on the arm.

Replacing the JSON geometry/moves does not require rewriting the renderer. Calibrated 3D execution would need a separately scoped renderer, rather than interpreting these SVG points as real TCP poses.

## Local preview

From `site-local`:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/projects/desktop-robotic-arm.html`. Use HTTP: the browser loads the separate JSON by fetch, so opening the HTML via `file://` is not the supported preview method. No build, framework, backend service, or external JavaScript dependency is needed for GitHub Pages.

## Validation

See `robotic-weaving-validation.md` for the completed browser and file checks.

## Pattern III correction
The user clarified that M1 / pattern-III.jpg combines multiple units; one completed unit is approximately X-shaped. The card and animation now show a schematic single unit with 17 mirrored top/bottom connections. Anchor count, equal spacing and zigzag visit order are visualization assumptions, not source data. The original combined drawing is preserved and linked. Need a single-unit source drawing or anchor-pair list to verify the exact geometry. Regenerate with tools/reconstruct-pattern-iii.py; the PDF extractor applies this override automatically. Earlier descriptions of the 64-chord composition describe the combined drawing, not the corrected animation.

## Hero photo cleanup
User requested the tight composition from codex-clipboard-4451f2d3-368d-428a-89fd-a907a42655cc.png, with the upper-right laptop removed. Used built-in image_gen (precise-object-edit). Output: assets/projects/robotic-weaving/weaving-hero-clean.png. Original execution photos remain unchanged. Only the hero reference and its caption/alt text were replaced.
Prompt: Remove only the visible upper-right laptop (keyboard, palm rest, screen fragment and shadow), seamlessly extending the beige tabletop. Preserve the supplied landscape crop, composition, robotic arm, mechanical parts, wires, fine suspended thread, weaving frame and woven threads. No added objects or redesign.

Hero aspect-ratio revision: weaving-hero-wide.png uses built-in image_gen tabletop outpainting. Prompt: extend only the beige tabletop left/right to 21:9; preserve the complete arm, base, tool tip, wiring, thread and woven frame without stretching; no laptop or new objects. CSS matches the reference 1800:771 display ratio. Previous image preserved.

## Pattern III — original-family selection (supersedes schematic X)
Restored the original combined image to the card. Animation now uses exactly M1.pdf extracted chord indices 40–46 (zero-based), a seven-line crossing family. Original normalized endpoint positions and frame are unchanged; no uniform spacing or new center intersection is imposed. Complete extracted composition is preserved in pattern-III-source.json. Visit order follows extraction order for reproducibility only, with schematic travel between threads; no robot program is inferred. Pattern I and II remain unchanged. The earlier 17-line schematic SVG is no longer referenced.

## User-marked sequence (supersedes extracted family)
Pattern III now follows explicit 06→36→35→05, then repeats the alternating rule down to index 0. Coordinates are approximate readings of the user annotated reference, with its landscape aspect preserved. Boundary links carry continuous thread and are solid; no lift/wrap/physical validation is inferred. Sequence is user specified, not a recovered robot program. Renderer displays the (edge,index) labels.

## Full reference / partial playback
All panels display complete patterns as toggleable pale references. I and II retain all 18 source chords but animate only the first 9 (one extracted half), yielding 17 moves each. III retains the exact approved 13-move marked sequence; its 64 original reference chords and reference anchors are rotated clockwise and mapped into the existing landscape frame. Reference geometry is independent of animated moves and does not advance the step count.

## Image and copy cleanup
Pattern captions standardized and rules shortened to one sentence each; detailed reconstruction assumptions remain in this document. Replaced the cluttered servo-wiring photo with original control-board.jpg technical artwork from DLB.pdf, updating alt text and caption. Execution 01–03 use SVG crop viewports to trim left/right edges (4.5/3.5%, 5/5%, 4.5/3.5% respectively); source JPEGs remain unchanged and full-size links show the same crops. No generated imagery was used for these edits.
