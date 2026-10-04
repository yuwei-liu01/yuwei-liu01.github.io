# Local validation — 2026-09-30

Validated with the in-app Chromium browser and a localhost static HTTP server. No remote push or deployment was performed.

| Check | Result |
| --- | --- |
| Correct project identity | Existing `desktop-robotic-arm.html` link matched against original portfolio pages 3–7; Fall 2024 / TENG TENG / Individual project retained |
| Three source patterns | I matched to triangular M2; II to clockwise-rotated M3 arch; III to M1 central opening; original drawings and completed SVG patterns visually compared |
| Independent playback | I and II started independently while the other panels kept their existing state; shared playback exercised all three |
| Pause/resume | Midway pause retained slider value 127 across subsequent reads; resuming continued from the existing position |
| Reset | Reset all returned every step and slider to zero; individual reset tested |
| Synchronized playback | All three restarted together and completed at the same normalized endpoint, including 4× playback |
| Speed | 0.5× and 4× exercised; selection changes the common timeline multiplier |
| Progress | Home / End and PageUp used on sliders; actual pointer drag moved II from 237 to 732 and updated to step 26 / 35 |
| Movement distinction | At I step 4, active movement was Reposition with SVG `stroke-dasharray="5 4"`; persistent thread group contains only weave moves |
| Final pattern | I and II show step 35 / 35; III shows 127 / 127; all reference thread connections remain visible at completion |
| Reference toggle | Unchecked reference group becomes `display:none`; independent checkbox state does not affect other panels |
| Pattern view switching | Selecting III hides I/II and resets all playheads; Compare all restores all panels; reference visibility is retained as a user preference |
| Desktop | 1440 × 1000: three panels aligned on the same row; no horizontal document overflow |
| Mobile | 390 × 844 and 320 × 780: no horizontal document overflow; panels stack, workflow steps align vertically |
| Themes | Dark and light project views visually checked; readable SVG thread, tool and target marks |
| Assets | No broken loaded images detected; all relative href/src targets in the three edited HTML files resolve to local files |
| JavaScript | Browser error/warning log empty after playback and interactions; `node --check` passes |
| Data invariants | Finite coordinates, unique anchor IDs, valid endpoints, contiguous successive moves, no duplicate chords; weaving moves exactly match reference connections |
| Homepage / All Projects | New title and requested card summary present; original `projects/desktop-robotic-arm.html` href preserved; no mobile horizontal overflow |
| Whitespace/diff | `git diff --check` passes |
| Protected other project | `multi-robot-construction.html` SHA-256 matches original checkout: `aed158dfb2a2a8d90813eb340c193607c0e7a909326283cc0db1def9c6943e75` |
| Original checkout / sources | Original checkout's five pre-existing untracked multi-robot assets remain unchanged; all edits are in `site-local`; source media were only read |

These checks validate a static website visualization. They do not validate real robot reachability, joint accuracy, collisions, tension, or execution of all three patterns.

## Reference-layout update

Adjusted only the weaving HTML and scoped CSS to follow the supplied reference: centered title and subtitle, blue date/type/instructor metadata, 800px justified introduction, full-width original execution photo, six section navigation links, and numbered section cards. Desktop (1440px) and mobile (390px) previews checked; anchors resolve, three animation SVGs load, no horizontal overflow or browser errors. Multi-robot page remains unchanged.
