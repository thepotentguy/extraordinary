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

## Deployment and limits — 25 October 2026

All five R3.2.1 themes were uploaded and published by the origin installer. Its final receipt records successful fresh-query verification of all 15 published CSS files against these frozen packages. Stored hashes were independently compared with the package members during this documentation update; no implementation or package byte was changed. See [DEPLOYMENT.md](DEPLOYMENT.md) for the clean release record.

Native result/rate-view checks at 320, 390, 768, 1024, 1440 and 1920px showed no horizontal document overflow for all five properties, without temporary CSS injection. Six-width home checks are also recorded. Imbali and Kingfisher home evidence was collected on R3.2; R3.2.1 subsequently changes only scoped booking-button margins. The remaining home checks use R3.2.1. The installed Imbali1920 alternative-date button matches its parent and has the verified 16px gap from the message.

Fresh-query matching does not certify rollout to ordinarily cached visitors. The installer observed an older Imbali stylesheet at an ordinary URL with `max-age=14400`; ordinary-cache propagation remains pending.

No logos or photographs were replaced. The blank CMS cropper and 0×0 validation occurred in both browser routes; editors were cancelled. Kwafubesi's native property gallery still shows 1/0 and mobile map issues remain unresolved in the vendor/native application. Missing mobileColor.css, physical touch, full accessibility and complete checkout remain separate. No booking or checkout write occurred. Publication and these bounded checks do not establish sponsor acceptance, production benefits or complete journey certification. Private installer evidence and screenshots are excluded from Git; only this reviewed aggregate is published here. This used round two of the approved maximum three review rounds.
