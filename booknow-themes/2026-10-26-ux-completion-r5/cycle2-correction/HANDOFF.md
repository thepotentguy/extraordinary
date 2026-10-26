# Cycle2 correction — native Pictures return state

26October2026, within the approved90minute/two-cycle envelope. This is the second correction/review cycle, not new scope. Prior frozen R5 remains intact.

Native evidence on Mabula desktop/mobile and Safari mobile shows: Terms closed → no visible detail panel → Pictures opened → Pictures closed → cached Terms unexpectedly visible. Native Pictures remains selected after the gallery closes. Therefore the older R4 description of this as restoring Terms is insufficient; the new before-state evidence proves a stale information panel resurfaces. The first R5 normal/short-panel geometry passes remain valid but do not certify this transition.

One scoped CSS rule hides the shared information table only while the native picture tab is selected. The separate native gallery remains visible. Selecting real Room Info/Location/Terms removes the picture selection and returns to the ordinary information-table rule. Actual Terms selection/unselection was verified on both native mobile routes. The direct-child information-table structure is grounded in retained native property markup, not invented HTML.

The patch adds no handler, JavaScript, HTML, image, room/rate data or focus semantics. All three ZIPs append this rule to the same three CSS files against independently published frozen R5 bases. Every other member is byte-identical. CRC and changed-member assertions pass; exact hashes are in release-manifest.json and packages/*-manifest.json.

Local state-sequence replay derived from observed selected classes:24cases,12R5 baseline stale-panel failures and12R5.1 corrected passes (three properties, desktop/mobile profiles,320/1440px). Corrected cases keep the gallery visible, prevent stale Terms behind/after it, and allow genuine Terms and Location to reopen. This is CSS state proof, not installed native-handler acceptance. The harness's selected-tab model was corrected to reflect native switching; no such code ships in the themes.

Publication remains origin-only after independent review. Verify ordinary applied R5.1 CSS before claiming a native corrected return path; fresh asset hashes alone are insufficient. Do not inject this CSS into a real page and label it deployed. Seven of12availability operations were used at handoff; known cached routes must not consume blind retries. Existing native overlays may be opened/closed read-only, with actual before/after postconditions. No booking/hold/payment/terms acceptance is authorised.
