R2 amendment: read CAPABILITIES.md and DESIGN.md first. New CSS page-entry effects respect reduced motion; native JavaScript gallery timing/loading does not change. Later-screen previews are authored offline fixtures, not native completed journeys. The exact R2 candidate and separate CMS changes need sponsor inspection before installer authority.

# Five property R2 candidates · review before installation

25 October 2026. These are OLD eRes/HTI BookNow themes. No installation was performed. Papi must inspect the five designs first. This chat has no Nebula/eRes administration write authority. The Clifftop-only exception in another chat does not transfer.

## Contents and bindings

Each `packages/<property>-Legacy-BookNow-R2.zip` has the existing `black-rhino2021/` root, 131 files and eight explicit directory entries. The historical folder name is a compatibility key, not the guest-facing property identity. Do not rename it or add an extra wrapper folder. There is no HTML or JavaScript in an installation ZIP. Native booking logic, links, hidden states, date controls and gallery runtime remain engine-owned. Embedded fonts use their accompanying OFL licences.

`source/themes/<property>/black-rhino2021/` contains the exact editable package members. `source/brands.json` records each official website reference, fonts, palette roles, voice and design rationale. `source/experience-layouts.css` contains the separate property compositions. `packages/*-manifest.json` records every member hash. A theme ZIP alone does not install the preview photograph, current logo or introduction copy.

Public home readback on 25 October verified `#header`, `#client_logo img`, `#nav`, `#searchBar`, `#stayCriteria`, `#unitBreakDown`, `#promoCriteria`, `#content`, `.imageCarousel #main` and native news-feed elements for all five properties. The header logo resolves to a CMS `published/site/` URL; carousel images resolve to CMS `published/imageCarousel/` URLs. Replacing a theme's fallback `images/colourSchemes/custom/logo.png` does not override that CMS binding. Runtime `simplegallery.js` and `createCarousel` are separate public engine assets; installation ZIPs do not replace them.

The previews use a frozen copy of each property's public header/search markup and the existing local public gallery runtime. No HTI application, tracking, login or checkout scripts are loaded. Proposed introduction uses native `.newsItemAnchor` and `.newsFeedItemDescription`, not an injected custom section. Verify that the target CMS news-feed fields retain the intended title/description before applying the copy; no arbitrary markup capability is promised. Existing news-feed content would also receive the theme styling.

## Separate CMS asset approval

Each `cms-assets/<property>/` contains:

- `logo-full-colour.png`: authentic full-colour official website mark, transparent whitespace trimmed, geometry preserved.
- `logo-230x100.png`: proportional compatibility export on a transparent 230×100 canvas. Use the full mark if the current CMS accepts it; check the displayed aspect ratio.
- `carousel-01-670x300.jpg`: proposed single people-free property photograph at the legacy guide's 670×300 size.
- `carousel-01-alt-crop-670x300.jpg`: alternate crop of that SAME photograph, for the local carousel mechanism demonstration. Do not install two near-identical crops as a production carousel. Choose one crop; preserve the existing native carousel and existing unreviewed frames until a later approved image selection.
- `property-133x99.jpg`: optional property thumbnail crop; this is not a verified room-type photograph. No room thumbnail replacement is supplied.

All images were inspected locally. Sources are recorded in `source/asset-sources.json`. These existing property assets are for the owner's property-branding use; no general stock-image or third-party redistribution licence is asserted. No people photography, excluded Clifftop image, fabricated review, offer, rate or inclusion is supplied. Introduction text is proposed copy in `source/brands.json`, subject to Papi's acceptance.

## Human installer gate and rollback

1. Obtain explicit property-specific theme/CMS authority and approval of the exact candidate version, commit and image/copy selection. Select the correct property; verify there are no unrelated pending changes that Publish would include.
2. Export/download its current theme, logo, carousel ordering/captions, property and room thumbnails and affected text. Record paths and SHA-256, verify archive contents and the actual restoration controls. The Clifftop rollback ZIP is NOT a rollback for these properties. No current per-property backups or restore tests were created by this design task.
3. Confirm current theme structure and desktop/mobile stylesheet load order against this package, with the vendor/human systems owner where needed. Upload the theme only in the authorised staging route. Keep CMS changes separate and bounded to the accepted assets/fields. Preserve native carousel configuration, timings, image links and pause/next/previous behavior.
4. Verify actual installed public `mainStyle.css`, `theme.css`, `mobileTheme.css` and `brand-fonts.css` against the manifest. Check ordinary URLs as well as cache-refreshed URLs. A successful upload is not proof that the CDN serves the new files. Do not republish just to flush cache.
5. Check each actual property at 320/390/768 and 1024/1440: header/logo, home and language controls, date picker, search, no-availability recovery, results, View Rates, horizontally contained rate calendar, terms, photo dialog, map, back/continue and permitted guest/consent/payment-layout steps. Use no booking/hold/payment action without separate authority. Check keyboard focus and readable text pairs. CSS cannot repair missing accessible names or engine behavior.
6. If a regression appears, stop the rollout and restore that property's verified backup through the authorised human route. Restore its CMS assets separately where changed. Verify ordinary public hashes and affected screens after rollback. Preserve the failed candidate and evidence; return the correction to Git rather than making undocumented CMS edits.

## Known limits

Local design/layout checks are not a live install test or sponsor acceptance. No availability search, guest data, booking hold, payment or confirmation was submitted in this work. Desktop Chromium viewport checks are not physical-device tests. Current room/result content, prices, eligibility, policies and existing gallery coverage were not audited for these five properties. No booking-performance benefit is claimed.

R4.2's mobile containment/guest-form fixes are retained. Its native Google Maps `mapDiv` initialization finding, missing resource/accessibility findings and untested end-to-end checkout remain open; this work does not fix or clear them. Browser support for `:has()` and modern CSS grid/flex should be confirmed against the client's supported device list; older browsers retain the underlying legacy fallback rather than all new home arrangements.

The downloaded public gallery libraries are local proof dependencies, not an extension platform or supported custom-JavaScript installation route. The theme cannot add Bigin integration, resident segmentation, exit prompts, new booking steps, reviews feeds, custom checkout logic, swipe or accessible control semantics by itself.

Canonical task identity and task-bound authenticated store remain unavailable, as recorded in the existing project binding. Local receipt is saved; canonical update and sponsor acceptance remain pending. Additional spending R0; included Codex allowance consumption unknown.

