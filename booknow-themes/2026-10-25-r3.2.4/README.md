# R3.2.4 — message dialogs remain centered after resize

A native inactivity dialog created at 1920px retained inline left:774px after resizing to 768/1024px. Its width was valid but its stale position put it outside the screen. Earlier message-dialog centering applied only through 640px.

This final patch centers non-gallery native message dialogs at every viewport size, with a viewport-height bound and internal overflow handling. Existing width, text, typography, colours and OK-button size remain unchanged. Gallery dialogs are explicitly excluded. No timeout or booking-state behavior changes.

The exact patch is appended only to mainStyle.css and root mobileTheme.css in each frozen R3.2.3 package. All other file bytes remain unchanged; each ZIP retains 132 files/eight directories. R3.2.3 mobile detail-panel repairs are preserved. Manifests contain exact package/member hashes.

Verification:

- Thirty local checks create the native-shaped inactivity dialog at 1920px with left:774px, then resize without rerendering through 320/390/768/1024/1440/1920px across five properties. Ten baseline overflows reproduced. All patched positions, containment, unchanged dimensions/text and button-size checks pass. Five local fixture OK-close checks pass.
- Six Pictures-dialog comparisons show no changes to geometry, position, transform, max-height or overflow.
- The coordinator tested the exact patch on actual pre-existing inactivity dialogs on all five native result pages: all 30 width checks pass. Actual Kingfisher OK closes at 768px without triggering a search. Those were native preview checks. All five final packages have since been published; see [DEPLOYMENT.md](DEPLOYMENT.md) for final published-style checks, the two retained overflow failures and partial acceptance limits.

Known limitations remain: Hamiltons/Hoyo old GPS values in native rate responses despite corrected saved CMS coordinates; the mobileColor.css 404 after the unsuccessful added-file hypothesis; and original-vendor draft editing before restoring the responsive package. This release does not fix those separate issues or claim universal cache rollout, complete accessibility certification, business improvement or sponsor acceptance. Earlier evidence and failed hypotheses remain preserved.
