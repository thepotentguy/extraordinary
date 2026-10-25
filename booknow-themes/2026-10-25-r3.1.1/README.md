# Five BookNow themes — R3.1.1 gallery copy correction

R3.1.1 replaces the internal empty-gallery caption “Shared legacy photographs” with **Photo gallery** in all five property themes. R3.1 and all earlier packages remain preserved.

Only the caption string changes in `black-rhino2021/css/mainStyle.css`, `theme.css` and `mobileTheme.css`: one replacement per file, 15 in total. The other 128 files in each package are byte-identical to R3.1. The complete R3.1 mobile-step correction is byte-identical. Desktop styling is unchanged apart from this intentional caption text replacement. Supplied native captions continue to display as supplied; the fallback applies only to an empty `.Caption` in a native gallery dialog.

Each ZIP retains 131 files, eight explicit directories and the legacy theme root. No application JavaScript, HTML, CMS content or booking data is included in the correction.

## Audit and checks

The CSS-generated customer-content audit covered every CSS member in all five R3.1.1 ZIPs: 50 files. `content-audit.json` lists the declaration selectors and values. No additional fixture, shared, legacy, Clifftop, prototype, placeholder, synthetic, offline, demo or internal wording was found in generated literal customer text. A manual review of the remaining nonempty literals found only “Photo gallery”, “Close details ×” and the existing Satellite map instruction. Empty pseudo-content, icon image URLs and nonliteral content categories are recorded separately. This is a CSS-content audit, not an audit of native application messages or CMS copy.

Thirty local browser checks passed: five properties × three changed stylesheets × 390/1440px. Exact shipping CSS displays “Photo gallery” for an empty caption and leaves a supplied native caption unchanged. All network requests were blocked in these local checks. Archive comparison proves only the three caption string replacements differ from R3.1; 640 other member files across the five themes are unchanged. Repeated builds have identical hashes.

`release-manifest.json` and `packages/*-manifest.json` contain the exact package/member hashes. `caption-verification.json` contains the browser evidence. Rebuild using bundled Python 3.12.14/zlib 1.3.2 and `source/build.py`, reading preserved sibling R3.1 packages; run `source/check-captions.cjs` for browser verification.

## Status

No theme was installed by this design chat. The origin installer independently established dialog absent → present with a native Pictures mouse click at phone width under touch-capable emulation. This remains mouse evidence, not finger-tap certification. Existing native touch, keyboard, map lifecycle, guest validation, payment and full checkout acceptance limits remain. Origin handles installation under its recorded approval, with its existing backup/rollback procedure; no new approval is requested for this correction.
