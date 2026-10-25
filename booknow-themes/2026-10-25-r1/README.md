# Five property legacy BookNow themes · R1

First inspection candidates for Kingfisher Villa Suites, Kwafubesi Tented Safari Camp, Hoyo Hoyo Safari Lodge, Hamiltons Tented Camp and Imbali Safari Lodge. Brand-first briefs were made from each official website on 25 October 2026. Five different compositions share the verified legacy structural/mobile foundation.

Open `index.html` or serve this folder locally and browse the comparison gallery. In the full local project pack, property links open frozen native-markup previews. In the clean Git handover, links open saved desktop/mobile proofs; private native DOM captures and public gallery runtime are not committed.

## Build and exact source

- `source/themes/<property>/black-rhino2021/` is the editable, complete source of that property's installation ZIP. This is the authoritative source for the reviewed artifact.
- `source/brands.json` gives positioning, visual character, palette, site typography, composition and tone, with official source URLs.
- `source/property-layouts.css` records the separately authored composition layers, already incorporated into each theme's desktop/mobile CSS.
- `source/assets/`, `source/asset-sources.json` and `cms-assets/` retain authentic property asset sources and proposed separate CMS exports. Font faces are embedded into `brand-fonts.css`; local sources and OFL licences are retained under `source/fonts/`.
- `packages/*-manifest.json` records ZIP SHA-256 and per-member hashes. `source/repack.py` rebuilds ZIPs from the exact editable source with fixed timestamps and directory entries, then compares against the reviewed hashes.

Use Python 3.12.14 with zlib 1.3.2 for the exact compressed archive bytes used here. Run `python source/repack.py`. No additional Python packages or network calls are needed to repack. A different zlib implementation can produce different compressed bytes even when every member is identical; the script reports this as a mismatch. Do not overwrite the reviewed manifest without reviewing the changed artifact. Per-member SHA-256 remains the content check across compression engines.

For a design revision, edit the property source CSS, repack into a NEW version, generate new manifests and rerun appropriate layout checks. Do not claim an old hash identifies a changed ZIP. `build.py` is the original authoring recipe; it can rebuild from the separately held R4.2 baseline after verifying its known hash, or use the already-generated source when the baseline is absent. `fetch-assets.py` is an optional bounded source-refresh recipe, not needed for offline reuse. Source refresh is a new design revision requiring asset review.

The full local pack also has `build-previews.py` and `verify-preview.cjs`: these depend on private captured public home DOM and the existing local proof runtime, so they are intentionally excluded from Git. Their saved layout results and images are review evidence, not a deployment certificate. The static gallery can be regenerated with `python source/gallery.py` using only the clean files.

## Verification and release boundary

All five local previews passed at 320/390/768/1024/1440 CSS pixels, with intended fonts loaded, visible fields at least 44px high and no horizontal page overflow. Each ZIP has 131 files and eight explicit directory entries under the expected legacy root, and contains no JavaScript/HTML. Actual native selectors and separate logo/carousel CMS bindings were inspected read-only for all five properties. Packaging tests and exact-source rebuild succeeded.

No live CMS writes, installation, availability search, booking, hold, payment or native checkout test occurred. Existing map/runtime and accessibility findings remain unresolved. No general portfolio release or business-effect claim is made. Per-property install compatibility, current policies/content and later booking steps require authorised human staging checks. Read `INSTALLER.md` before any release. Papi's design acceptance remains pending.

Existing marks and property photography remain owned by their respective owners and are supplied for the authorised property-branding work; no unrestricted stock/image licence is granted. Retain font OFL and existing third-party software notices. R0 additional spend; included Codex allowance use unknown.
