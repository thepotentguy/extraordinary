# R3.2.1 — round-two native button-margin correction

Minimal follow-up for all five accepted BookNow designs. R3.2 and all prior packages remain unchanged.

The actual native Imbali1920 alternative-date button inherited `margin:6px 3px 0 -42px`, shifting it42px outside its parent and26px into the no-availability message. The round-one test checked viewport containment but missed this parent/overlap condition.

`source/button-margins.css` sets `margin:0!important` on four scoped native button classes: the no-availability alternative-date button, the hotel-rate standard button, View Rates links and room-rate small buttons. It changes no colour, font, size, padding, border, brand treatment, grid, photograph, logo, dialog or native application state. Every existing R3.2 CSS byte remains as its exact prefix; only this five-line layer is appended to mainStyle.css/theme.css/mobileTheme.css. All other128files/property (640total) remain byte-identical. Each package still has131files/eightdirectories and noHTML/JS.

## Focused evidence

- `button-margin-audit.json` reviews132legacy margin declarations matching those four button classes across all five shipping theme CSS sets. All five contained the negative alternative-date margin and earlier negative View Rates margins; other positive/auto values are retained in the audit.
- Five R3.2 baseline cases reproduce the new parent-containment/overlap failure at1920px before the fix. All90targeted R3.2.1 cases pass: five themes × no-availability/result/rates layouts ×320/390/768/1024/1440/1920px.
- The check now asserts every visible scoped button fits within its own parent on all sides, does not overlap the adjacent message/rate text, and has zero computed margins. A native-class View Rates row is explicitly added in the authored rate-state fixture. No availability, price or native navigation is supplied by it.
- Fifteen HTTP stylesheet hashes match exact ZIP member hashes. Repeat package builds match. Version/member hashes are in `release-manifest.json` and `packages/*-manifest.json`; test details and preserved failing baseline are in `verification.json`.
- Origin independently previewed the exact patch on actual Imbali1920 DOM: button edges match its parent, the adjacent message has a16pxgap, and computed margin is0. The temporary style was removed. This is independent native preview evidence, not R3.2.1 deployment evidence.

The targeted run is limited to affected button layouts. R3.2's other geometry, home-photo, logo and dialog evidence remains in its preserved folder; no broad retest or redesign is claimed.

## Review and build

Local preview: `http://127.0.0.1:9148/previews/imbali/journey.html?screen=noavailability` (substitute any of the five property IDs). Exact shipping CSS is under `package-css/<property>/black-rhino2021/css/`. Screenshots: `previews/<property>/noavailability-390.png` and `noavailability-1920.png`.

Rebuild with bundled Python3.12.14/zlib1.3.2: `source/build.py --extract-for-review`, reading preserved sibling R3.2 ZIPs. `source/prepare-review.py` reuses R3.2 native-shaped journey fixtures, sources and preview assets; serve this directory locally on9148 and run `source/check-buttons.cjs` with the bundled Playwright runtime. Original fixture nesting/classes are preserved.

## State and limits

At this handoff origin reported R3.2 published/hash-verified on Imbali, Kingfisher and Kwafubesi; Hamiltons/Hoyo Hoyo had not yet received R3.2. R3.2.1 is a separate frozen candidate; this design chat performed no CMS operation or new availability search. Origin owns subsequent installation, rollback, native checks and the shared search count. Consult its dated installation receipt for later per-property state.

Ordinary CSS URLs still served an older Imbali release at the origin's latest check (`max-age=14400`, `age=3552`), while fresh URLs matched the installed R3.2 candidate. Fresh verification does not establish rollout to all visitors. Ordinary-cache propagation remains a separate pending check.

The CMS cropper/asset blocker, Kwafubesi empty property gallery, native map lifecycle, missing mobileColor.css, physical touch, full accessibility and complete checkout remain separate. Local fixture passes and the native margin preview do not establish sponsor acceptance, production benefits or complete journey certification. This is round two of the approved maximum three review rounds.
