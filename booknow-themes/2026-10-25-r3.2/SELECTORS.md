# R3.2 structural repair selectors

| Native structure | Cause | Reviewed correction |
|---|---|---|
| `.hotelResult > .hotelNoRatesResult:has(>.leftColumn)` | Shared photo-row selector also matches no-availability row; higher specificity forces133px grid track | Explicit flexible message row, no grid columns, native DOM order |
| `.hotelNoRatesResult > .leftColumn / .rightColumn` | Text/button cannot grow or wrap inside inherited track | Flexible bounded columns; full-width mobile items; hidden native controls untouched |
| `.hotelImage`, `.hotelImage img`, `.hotelResultRoom .roomImage img` |133px image plus12px padding and wrapper margin exceeds133px track | Remove padding/margin/background; contain actual image, max133×99, no enlargement |
| `.hotelDescription p`, `.hotelNoRatesResult .info`, buttons | Legacy floats/fixed widths and long text | Bounded normal wrapping; min-width0; intentional inner date-grid scrolling retained |
| `.steps > div[class*="stepsName"] > div` and `.steps > .gwt-Label` | Absolute84px selected sprite inside72px parent, negative6px, stale animation offsets | Hide empty decorative nodes; remove old background image; keep native labels/actions |
| `.steps > div[class*="stepsName"] > a::before` | Missing/inconsistent legacy sprite geometry |24px numbered badge inside each existing anchor;48px label target; mobile inactive wrappers hidden |
| `.imageCarousel`, `.imageCarousel #main`, `.gallerylayer img` | Legacy full-width and Imbali670/260 aspect override enlarge/distort670×300 derivative | Max670px stage;670/300 ratio; object-fit contain; distinct surrounding brand layout retained |
| `#client_logo img`, `#header` | Old JPEG aspect/height applied to differently proportioned full PNG | Intrinsic ratio, natural-size cap, growing header; CMS URL remains owner controlled |
| `.gwt-DialogBox:not(:has(#gallery))` | Legacy95% root at tablet width and370px inline table diverge; phone overflows | Fit-content base; phone viewport-bound292px at320; independent non-gallery scope |
| Non-gallery dialog side/center cells | Fixed table layout shares width between three equal cells |1px decorative side cells; main text column uses remaining width |

No handler, DOM node, booking state, rate, quote, consent state, map initialization or CMS content is changed. Badges are visual numbering of the four existing native step labels, not new journey stages. The stylesheet does not add native keyboard semantics or certify screen-reader behavior.
