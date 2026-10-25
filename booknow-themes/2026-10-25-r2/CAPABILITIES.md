# What R2 actually delivers

This is legacy BookNow. The native booking order is unchanged across all properties. The experience differs through composition, grouping and presentation of existing elements. The five property directions are compared in `DESIGN.md` and alongside the gallery.

| Treatment | Installable theme ZIP | Separate CMS setup | Vendor/runtime support |
|---|---|---|---|
| Hero size, crop window and framing | CSS aspect ratio, image fit, outlines, existing frame surfaces | Accepted source image and 670×300 export; captions and order | Higher-resolution carousel source sizes require vendor confirmation before expanding past the legacy guide |
| Carousel controls/captions | Place/style native Prev, Play/Pause, Next and counter; inset caption, field note, attached block, folio caption or dark shelf | Correct property caption and image targets | Autoplay timing, pause-on-load, loading order, transition algorithm, swipe and keyboard semantics |
| Information entering a page | Brief CSS reveal on existing `.animated` content class; reduce-motion media query disables added motion | None | Class/event timing and asynchronous fetch order remain native; no simulated data loader is supplied |
| Booking arrangement | Existing search panel as right column, full-width planning bench, bold left block, top itinerary strip or dark booking band | Current labels/content remain native | Different search logic, new steps, submit behaviour and server loading state |
| Results and rooms/rates | Suite dossier/rate column; stacked field guide; colour-block sections; ruled ledger; broad information/rate bands | Verified current description, room photos, rate terms remain engine/CMS-owned | New rate-comparison logic, room sorting, inventory, prices, totals and eligibility |
| Terms | Inset sections, dashed field notes, paired colour blocks, two-column folio or dark headings | Current terms attached to the selected rate | Policy logic/terms acceptance |
| Pictures | Five photo-dialog mats, header treatments and contained native dialog | Existing gallery coverage and approved image selection | New gallery interaction, native event handling and accessible dialog focus management |
| Location | Split map/facts, stacked map/facts, broad map block, framed map plate or adjacent zones | Verified current directions/contact content | Map initialization and network integration; existing `mapDiv` finding remains open |
| Progression | Existing native step labels, current/unselected state and Back controls are restyled | None | Different step order or checkout logic |

## Preview integrity

Home previews reuse the already reviewed property-specific frozen home/search markup and public native gallery runtime locally. No runtime change is installed. Later previews use authored neutral fixtures with the observed native selectors, not scraped operational pages or customer records. Their local review tabs and handlers are explicitly outside the installation ZIPs.

The fixture's View Rates, Terms, Pictures, Location and Close controls switch local views. The rate total says “Not loaded”; policies describe where verified native text belongs; the map is a clearly marked placeholder. Room selection is disabled. These are layout and navigation demonstrations, not an alternate booking engine or a confirmed native end-to-end test.

One source photograph per property is reused from R1. A second crop demonstrates the existing native carousel only. Do not install near-identical frames as a production gallery. No new asset sourcing, people photography, room-identity claim, review, offer or rate is introduced.

## Motion and safety boundaries

New CSS content reveals are 170–250ms and disabled for reduced motion. Button shrinking animations were removed from essential actions so they remain legible and touch-sized. This does not establish that the existing JavaScript carousel respects reduced motion: autoplay, timing and its native fade are unchanged and require vendor support for a reliable reduced-motion policy.

Inline native hidden states are retained. No required booking fields or controls are hidden for visual effect. The wide rate grid scrolls inside its own panel. CSS-only styles cannot fix missing programmatic accessible names or certify the native checkout.

No live installation, CMS write, availability query, booking, hold, payment, cancellation or confirmation occurred. The permanent Nebula/eRes read-only boundary applies in this chat. Sponsor inspection/acceptance, a separately authorised installer, actual property backups/rollback and native regression testing remain necessary.
