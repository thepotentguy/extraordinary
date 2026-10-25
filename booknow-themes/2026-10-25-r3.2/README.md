# Five BookNow themes — R3.2, repair round one

Frozen CSS repair candidate for Kingfisher, Kwafubesi, Hoyo Hoyo, Hamiltons and Imbali. All five brand palettes, typefaces, navigation treatments and distinct photograph controls remain. Earlier releases are preserved. This design chat has not installed R3.2.

## What changes

- The native no-availability message no longer inherits the 133px photograph grid track. It wraps in a flexible message/action row and precedes the photograph on mobile.
- Native 133×99 thumbnails lose inherited padding/margins that pushed them outside their wrapper. Images retain their aspect ratio and are not enlarged beyond their source raster.
- Native step labels stay in their own wrappers. Old empty sprite/animation nodes and divider footprints are hidden; aligned numbered badges sit inside the existing native anchors. The mobile current-step-only model and native action visibility remain.
- Home photographs are contained at up to 670×300 with their correct ratio; existing smaller screens shrink proportionally. Imbali's conflicting 670/260 ratio is overridden. No larger source, sharpened image or new CMS photo is invented.
- Logos retain their actual source proportions, fit inside the existing brand header, and are not upscaled, cropped, filtered or recoloured. The header can grow for a full 4:3 mark.
- Non-gallery native message dialogs now fit phone/tablet viewports. Their legacy side cells no longer divide the message into a narrow middle third. OK remains visible and naturally keyboard-focusable. Internal rate-calendar scrolling remains intentional and contained.

Exactly three CSS members change per property: `black-rhino2021/css/mainStyle.css`, `theme.css`, `mobileTheme.css`. Each is the entire R3.1.1 file followed by the same reviewed `source/round1.css` layer. All other 128 files per theme (640 total), including fonts, images and brand assets, are byte-identical. Each ZIP keeps 131 files and eight directories; no HTML or JavaScript is installed.

## Evidence

The exact native Imbali result supplied by the installer contains both the no-availability message row and the following image/description row, including hidden rates, feature icons, information links and native detail table. The idle dialog retains the native 370px inline table. Step fixtures retain native selected/animation children, divider nodes and hidden actions. These replace the earlier simplified result/step assumptions.

The local R3.1.1 baseline reproduces the installer's measurements exactly: message client133/scroll364px; image wrapper125px with137px image; selected marker84px in72px wrapper; idle page377px at320px; Imbali home1260×488.953px at1440px. See `baseline.json`.

Final evidence covers 270 layouts (five properties × nine states × six widths320/390/768/1024/1440/1920), 120 step-state permutations, ten local recovery/keyboard checks, 12 original-PNG logo geometry checks and 15 exact HTTP/ZIP CSS hashes. The last change only adjusts non-gallery dialog width to fit-content: all30 affected idle cases were rerun. The five preceding tablet failures remain in `verification-before-tablet-dialog-fix.json`; final aggregation and scope are explicit in `verification.json` and `verification-summary.json`.

Stable home screenshots wait for every nested native image ancestor to finish its fade. No brightness filter or photograph-obscuring overlay was added/removed to make a screenshot look clearer. Source pixels and the dark Imbali caption shelf remain intact. Two-frame home proofs use the previously approved local photograph crops; they are not evidence that CMS photos were replaced.

Local preview: `http://127.0.0.1:9147/`. Exact extracted CSS: `/package-css/<property>/black-rhino2021/css/`. Proofs: `previews/<property>/{home,noavailability,photos,idle}-{390,1440}.png`. Transparent-logo screenshots are preview-only original-source substitutions, not deployed CMS assets.

## Build and review

`source/build.py --extract-for-review` rebuilds from preserved sibling R3.1.1 ZIPs using bundled Python3.12.14/zlib1.3.2; repeat builds have identical hashes. `source/check-round1.cjs` uses the bundled Playwright installation and local preview service. The full home proof also uses the existing local R3 captured home structure and original gallery runtime, which are excluded from the public repository. Public packages, patch, exact changed stylesheets, native result/idle/step fixtures, labelled journey fixture and screenshots remain reviewable. Full local replay requires the original workspace proof inputs; no claim of a self-contained public native application is made.

## Open acceptance items

Origin independently previewed the native repair: Imbali1920 message133/364→726/726px, aligned48px step anchors, and mobile320 idle page377→320px with292px dialog and258px text. Those temporary overrides were removed; these are preview observations, not deployment evidence.

The original transparent Imbali/Kwafubesi PNGs are preserved. The CMS cropper displays blank and reports0×0 in both browser routes, including editing an existing carousel image before upload; no asset replacement success is claimed. There is no logo-dimensions descriptor in either original/release ZIP;230×100 was an old image size, not a verified crop requirement. No vendor bypass, guessed target size or white background is used.

Native map lifecycle, Kwafubesi's empty property-gallery data, missing `mobileColor.css`, physical touch, full keyboard/screen-reader accessibility and complete checkout remain separate. Passing local fixture checks does not certify those behaviors or business benefit. Origin handles the next bounded native review under the existing three-round envelope. No availability search, extra agent or paid route was used here.

At final handoff the origin reported that R3.2 upload remained on the spinner in both browser routes, without success or pending publication changes. No Publish action or R3.2 live result was reported. This is a separate deployment blocker; the frozen candidate is not changed to work around it.
