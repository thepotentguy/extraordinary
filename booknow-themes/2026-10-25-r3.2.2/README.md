# R3.2.2 — missing native mobile stylesheet

Adds only `black-rhino2021/css/colourSchemes/mobileColor.css` to each frozen R3.2.1 ZIP. All 131 original file contents remain byte-identical. Each package now contains 132 files and eight directory entries.

The native mobile HTML requests this path, although the packages lacked it. The mobile shell already loads shared `colourSchemes/color.css`; accepted property styling remains in mobile.css/mobileTheme.css. The added file intentionally contains comments only, preserving the existing palette rather than inventing duplicate overrides. This supplies a requested compatibility resource; native publication and HTTP-404 recovery must be verified separately.

Local verification: ZIP integrity/member-difference assertions pass. Thirty comparisons across five properties at 320/390/768/1024/1440/1920px passed with authentic transparent 230×100 native-logo fixture images. The added stylesheet returned 200 locally and parsed zero rules; all measured geometry, colors, backgrounds, fonts and spacing stayed identical without document overflow. Initial comparisons observed animation timing differences; that output is preserved. The final comparison disables animation/transition only in the local measurement harness, with 30/30 passing. No animation behavior is changed in the packages.

The existing [native editing workflow](../2026-10-25-r3.2.1/CONTENT-EDITING.md) still applies. This release does not repair the legacy CMS stylesheet parser or the stale/other-source GPS values observed in native rate responses. There is no HTML, JavaScript or booking-state change.

`release-manifest.json` and package manifests record exact ZIP/member hashes. `source/build.py` builds deterministic packages; `source/check.cjs` supplies the bounded local regression check. Actual content editing and publication belong to the authorised coordinator. This is local verification, not sponsor acceptance or a claim of business improvement.
