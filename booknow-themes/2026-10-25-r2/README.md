# Five property BookNow experience themes · R2

This is the requested consolidated creative revision of the same five themes. The existing website-based brand briefs and authentic assets were reused. R1 is preserved under `booknow-themes/2026-10-25-r1/` in Git and its original local folder. It is not overwritten or marked accepted.

Open `index.html` for the comparison. Each property has desktop/mobile previews for Arrival, Stay options, Room & rates, Terms, Pictures and Location. Later-screen links open working, clearly labelled offline fixtures. Home runtime previews are local only; the clean Git pack uses saved home proofs and working authored later-screen fixtures.

## Material changes

- Kingfisher: framed villa view and inset caption with vertical square controls; right booking column; suite dossier with separate rate rail; light inset details.
- Kwafubesi: canvas panorama and field-note caption; horizontal planning bench; stacked room blocks and rate band; dashed detail sections.
- Hoyo Hoyo: paired architecture/welcome blocks and attached square controls; strong left booking block; accent rails, segmented information controls and paired policy blocks.
- Hamiltons: top itinerary-planning strip, double-framed hero and folio caption; room/tariff ledger; fine ruled terms/map/photo plates.
- Imbali: photographic stage with dark caption/control shelf and booking band; broad rate sections; dark picture mat and adjacent map/facts zones.

`DESIGN.md` records the comparison and rationale. `CAPABILITIES.md` separates CSS, CMS and vendor requirements. The native sequence and runtime are unchanged; five different checkout sequences or loading engines are not promised.

## Build

`source/themes/<property>/black-rhino2021/` contains the exact editable installation source. `source/experience-layouts.css` is the separate R2 identity-through-the-journey layer, appended to desktop and mobile themes. `source/build-r2.py` deterministically repackages the source and records all member hashes. Run it with Python 3.12.14 and zlib 1.3.2 for the reviewed archive bytes; other compression libraries may produce different ZIP bytes for identical members.

All five ZIPs retain 131 files and eight explicit directory entries under the historical `black-rhino2021/` compatibility root. No HTML or JavaScript is installed. Fonts and OFL licences remain embedded/included. CMS logos, photos, captions and introduction are separate accepted setup items.

`source/build-fixtures.py` and `source/fixture.js` generate the synthetic later-screen previews. Their event handlers are review tools only; they do not contact eRes and must never be inserted into the theme ZIP. Their content is neutral: no real room/rate/inclusion/policy/availability data. The property thumbnail is explicitly not a verified room image.

## Verification and next gate

See `verification-summary.json` for measured layout/motion/fixture-navigation checks. These are local Chromium desktop viewport checks, not physical-device tests, vendor import acceptance or native booking certification. Original R4.2 containment and guest-form safeguards remain in the packages. The native map initialization finding, native carousel accessibility/motion handling, current policy/rate correctness and checkout remain open.

Review R2 before any installation. `INSTALLER.md` retains the per-property authority/backup/rollback/native test gate. R0 additional spending; included allowance consumption unknown. No further agents, paid routes, new research sweep, live edits or transactions. Canonical task identity/destination remains unavailable; local handover is saved and canonical update pending. Sponsor acceptance is separate.
