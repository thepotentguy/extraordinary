# R4 publication and qualified native verification

26 October 2026. One approved three-property repair increment. Six new read-only availability operations were used: one existing desktop-result reload and one native mobile search per property. Each search used 23–24 November 2026, one room, two adults and zero children. No further query, View Rates, booking, hold, payment or terms acceptance was performed. Earlier audit ledgers remain separate.

## Deployment identity

The origin chat independently reviewed the CSS-only archives against fresh rollback exports, accepted desktop/320px visuals and published all three. Fresh published custom.zip hashes equal the frozen candidate hashes in release-manifest.json. All nine freshly fetched changed CSS files also match the candidate bytes exactly; see evidence/fresh-published-assets.json. A fresh asset URL is not proof that an ordinary page applies that asset.

## Actual applied styles

| Property | Desktop result | Native mobile result |
|---|---|---|
| Mabula | R4 applied through ordinary theme.css; older mainStyle.css remains cached | R4 applied through ordinary mobileTheme.css; older mainStyle.css remains cached |
| Safari Plains | Older mainStyle.css and theme.css applied; R4 live verification pending cache refresh | R4 applied through ordinary mobileTheme.css; older mainStyle.css remains cached |
| Angels View | Older mainStyle.css and theme.css applied; R4 live verification pending cache refresh | Older mainStyle.css and mobileTheme.css applied; R4 live verification pending cache refresh |

Angels View's ordinary desktop page still measured document441/table417 at viewport320. This is retained failure evidence, not an R4 live pass. Fresh R4 asset URLs have the right bytes. Ordinary CSS responses showed substantial server cache Age values; no CSS was injected or substituted to create a native pass.

## Verified native behavior

For the three routes actually applying R4, 18 result observations cover 320/390/768/1024/1440/1920px. Document width equals viewport width throughout. Mabula desktop's summary table is261px at320px, compared with417px before repair. Native Book/Book Now controls are visible and46px high; they were measured without clicking. Visible mobile Total Stay prices remain readable. Public prices are observation evidence, not quotes or availability guarantees.

60 native panel observations cover Mabula desktop Room Info/Location/Terms/Pictures and Mabula/Safari mobile Location/Terms/Pictures at the same six widths. Every panel fits the viewport and Close is hit-testable at internal-scroll start/end. Seven native detail Close actions removed the panel. Three Pictures Close actions removed the gallery and restored the previously open Terms panel. The initial strict panel:null check returned false in those three cases; it is preserved because gallery removal, rather than removal of the underlying Terms panel, is the correct postcondition. A follow-up independently confirmed no visible gallery on all three routes.

The real mobile result layout does not expose Room Info or a visible desktop room-summary table. The unchanged native mobile CSS directly hides that TABLE. Local mobile-profile table/price checks are therefore N/A, not visible mobile-table passes; local results certify panel/document geometry only. Mobile Room Info cannot be accepted from replay markup.

Safari Location reports that GPS coordinates are unavailable for this hotel and renders no map tiles. The address/contact panel is contained. No coordinates, routes or master data were invented or changed. Mabula map/frame checks do not certify coordinate accuracy.

## Visual evidence

- evidence/mabula-live-roominfo-320.jpg: genuine ordinary native desktop route applying R4, at320px.
- evidence/safari-live-mobile-location-320.jpg: genuine ordinary native mobile route applying R4, at320px, showing the missing-GPS message.
- evidence/angels-roominfo-320.jpg: clearly local design-review proof, not live Angels acceptance.

## Remaining acceptance

Angels View desktop/mobile and Safari desktop need ordinary-page cache convergence and subsequent verification in a separately authorised query envelope. Alternate-rate/calendar states, checkout, physical touch/wheel gestures, full assistive-technology/focus behavior and geographical accuracy remain unverified. CSS does not supply missing modal semantics or focus management. Sponsor acceptance remains separate from implementation and review. Required canonical task/memory write remains pending because a verified bound canonical destination was unavailable; the project receipt is retained locally.
