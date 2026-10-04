# Hardware & Control redraw

Layout follows the supplied reference: large exploded arm at left; threading tool at upper right; controller, servo and PWM schematics below. Original CAD linework was extracted as SVG from 素材/bzt.pdf, endeffector1.pdf, DLB.pdf and dj section.pdf. All geometry remains vector paths. Source files are preserved. Stroke weights were normalized for screen readability. Computer/power symbols, connections, servo horns and qualitative waveforms were redrawn as editable SVG elements.

Only weaving hardware appears. Suction equipment is omitted. Unverified axis ranges, torque ratings, voltages and pulse timings are omitted. Waveforms show qualitative pulse-width differences, not calibrated angle-to-pulse mappings. Computer serial commands and controller servo signals are separate stages. Power connection is conceptual, not a verified wiring/pinout diagram.

Deliverables: hardware-control.svg; hardware-control.png (3200×2500); hardware-sources/*.svg; tools/build-hardware-control.py. Page and project CSS embed the new figure with SVG/PNG full-size links. Existing serial code excerpt is retained.

Detail revision: added source axis/motor mapping (Axis 2 has Motors 2 and 3), conceptual motor-to-controller leads, supply meter/plug and a power-switch callout. Redrew a labeled servo section showing horn, gears, potentiometer, motor, board and microcontroller; placement is schematic rather than an internal manufacturing drawing. Numeric ratings remain unverified and omitted. PNG now 3200×2900.

Correction: removed the standalone axis/motor table. Seven dotted leaders now originate at the corresponding motor bodies in the exploded drawing and continue to the controller, with axis/motor names placed alongside each leader.

Axis/board detail: Axis 3 lead is horizontal. Source-reported ranges added: A1 0–270°, A2 10–110°, A3 20–145°, A4 0–180°, A5 0–155°, A6 0–180°. Caption distinguishes these from verified limits; no IK model limits changed. Board labels transcribed from supplied close-up: USB, ON, GND, 5V, TX/TR, S1–S24 and polarity marks; this is a drawing transcription, not verified wiring advice.

User correction: Axis 3 / Motor 4 horizontal leader moved down to y=742, aligned with the third servo row S3. Motor anchor and label moved with the line to preserve its straight shape.

Latest revision: removed the complete Inside the Servo panel and tightened canvas to 1600×1270 (PNG 3200×2540). Axis 4 / Motor 5 now starts on the far-left motor case. Seven motor cases receive editable pale blue-gray polygon fills beneath the original linework. Axis 3 remains horizontal to S3; source files are unchanged.

Layout refinement: computer and meter/plug redrawn following supplied detail, continuous USB lead and black/red supply leads terminate on the board; switch callout points to existing board switch. Removed all three outgoing servo lead strokes. Reduced threading-tool drawing to 410×205 at upper left of right panel. No unverified supply-voltage range added.
