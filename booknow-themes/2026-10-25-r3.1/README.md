# Five BookNow themes — R3.1 mobile steps correction

R3.1 restores the native mobile current-step layout. R1, R2 and R3 remain preserved. No installation was performed by this design chat.

Each of the five packages changes only `black-rhino2021/css/mobileTheme.css` relative to R3. The correction hides native inactive steps, empty dividers and decorative animation blocks at widths up to 960px. It keeps the current label and any native eligible Back/forward actions in normal layout, at least 44px high. Native hidden actions remain hidden. Property Terms, Pictures and Location controls are unchanged.

All 130 other files in each package, including desktop theme CSS, fonts, images and base styles, are byte-identical to R3. Each archive retains 131 files, eight explicit directories and the legacy `black-rhino2021/` root; no JavaScript or HTML is shipped in the theme ZIP.

## Verification

- 180 local layout permutations passed: five properties × 320/390/768px × four current labels × no action/Back/forward action. The starting DOM preserves the actual native mobile result-stage inactive classes, empty divider/animation nodes and hidden actions supplied by the installer.
- Later label/action permutations are synthetic geometry checks; they do not assert that a particular action is eligible at a particular real booking stage. No native state transition or business transaction is exercised.
- No hidden action or inactive step was exposed; one current label remained visible; eligible tested actions were at least 44px high, without overlaps or horizontal page overflow.
- Five 1440px computed-layout comparisons were identical with and without the correction. Archive comparison independently verifies desktop CSS and all other members are unchanged.
- Kingfisher local replay measured 170px before and 68px after at all three widths. The installer's separate native live test measured 206px before; this local result is not a live after measurement.
- The existing R3 authored result fixture alone omitted native state/detail nodes. R3.1 adds `source/native-steps.html` and explicitly tests those nodes and classes rather than relying on the earlier simplified fixture.

Exact hashes and member comparisons are in `release-manifest.json` and `packages/*-manifest.json`. Detailed local results are in `verification.json`. Rebuild with bundled Python 3.12.14/zlib 1.3.2 using `source/build.py`; it reads the preserved R3 packages. `source/check.cjs` uses the existing local R3 preview service on port 9145 and the bundled Playwright installation. No live service queries are used.

## Installation handoff

The origin installer chat retains its recorded installation approval. As reported there on 25 October, Kingfisher's R3 trial was rolled back and ordinary/fresh public CSS hashes match its original backup; the other four were not changed. All five production themes remain original at this handoff.

Before rollout, the installer should establish dialog-absent → dialog-present using the native application, distinguish mouse clicks from actual touch taps, verify current-step/action layout on native mobile DOM, retain backup/rollback evidence and check ordinary versus fresh CSS delivery. This correction does not itself certify native touch, native keyboard support, map lifecycle, guest validation, payment or complete checkout. See `INPUT-READINESS.md`.
