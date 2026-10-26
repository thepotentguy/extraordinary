# Three-property booking journey repair R4

Room/rate tables previously expanded beyond narrow desktop-route viewports. Native details could open below the viewport and hide their Close control. This release contains narrow tables and uses a viewport-relative, internally scrollable detail shell with a sticky48px Close header. It preserves each property identity, native handlers, all existing images/rates/content, and Mabula Scroll R3.

Only mainStyle.css, theme.css and mobileTheme.css append source/native-panel-repair.css. All other archive members are byte-identical to the verified bases. Full editable theme source is in package-css, complete installable ZIPs and member hashes are in packages. See release-manifest.json for exact ZIP hashes. No HTML, JavaScript or executable is added to an installable theme.

## Build

Run Python3 source/build-repair.py from this folder. It uses exact verified sibling releases: 2026-10-26-mabula-scroll-r3 for Mabula and 2026-10-26-three-properties-r2 for Safari Plains/Angels View. The public script adapts only this sibling directory name; its output ZIPs must match the frozen SHA256 values. No dependency installation is required.

## Evidence and acceptance

Three properties, separate desktop/mobile stylesheet profiles, six widths and five states produced180local geometry observations. Mobile baseline directly hides the desktop TABLE, so local mobile table/price readability is N/A. These fixtures are not actual mobile application acceptance. Final JSONs explicitly retain that qualification. Actual native verification is recorded separately in LIVE-VERIFICATION.md.

All three archives were independently reviewed and published. Fresh archive and nine changed CSS hashes match. Ordinary native pages applied R4 on Mabula desktop/mobile and Safari Plains mobile. Their18result observations and60panel observations passed the scoped containment/Close checks. Angels View desktop/mobile and Safari desktop still applied older cached CSS and remain pending live verification. This is not blanket release acceptance or proof of global cache convergence.

Native mobile exposes Total Stay/Book plus Location/Terms/Pictures, with no Room Info link. Safari has no GPS coordinates in its native Location data. No data correction was made. Alternate rates/calendar, checkout, physical gestures and full focus/accessibility behavior remain unverified. The six-operation availability allowance is exhausted; no further query is part of this release.

Local design proof: evidence/angels-roominfo-320.jpg. Genuine ordinary native proof: evidence/mabula-live-roominfo-320.jpg and evidence/safari-live-mobile-location-320.jpg. Public price observations are dated evidence, not quotes or availability guarantees. No guest, booking, authentication, operational mailbox or private chat records are included.

Sponsor acceptance and canonical project persistence are separate pending controls. This draft PR is for review, not authority to merge or to run additional production actions.
