# Native input findings — 25 October 2026

The public Kingfisher desktop and mobile entry points loaded the same native GWT permutation `AF74838F14DC78B26E209462987827E0.cache.js` during bounded read-only inspection. No availability search, CMS access, booking or payment was performed by this design chat.

Native `ResultSummaryViewMobile` supplies the Pictures, Location and Terms anchors through `kf`, `hf` and `jf`. Shared `ResultSummaryPresenter` attaches click handlers to those methods. The native Pictures handler constructs the property picture view; Location and Terms populate their native content panel. The installer independently observed `__eventBits: 1` and an `onclick` function on each anchor. Their absence of `ontouchstart`/`ontouchend` is not evidence of a broken link: browsers normally synthesize a click after a tap.

The installed official Chrome DevTools MCP click implementation uses a Puppeteer locator click (`build/src/tools/input.js`, line 163), which emits mouse events. The installer's event logger recorded trusted pointerdown/mousedown/pointerup/mouseup/click with `pointerType: mouse` while `navigator.maxTouchPoints` was 1. This was a mouse test in a touch-capable emulated environment, not an actual finger tap.

Previous non-response reports therefore do not establish missing native handlers or a CSS defect. A dialog count of one also cannot prove a new action when a dialog was already present. Start with no dialog, record the input sequence, perform one Pictures activation, and verify a new dialog and usable close/control targets. Test actual touchscreen input separately. Emulation changes can reload the document and clear injected stylesheet links or application state; record the active CSS hashes and input mode after any change.

Recommendation: retain the supported property links, apply only the separately verified mobile-steps correction, and keep native touch acceptance pending until trustworthy tap evidence exists. CSS cannot attach handlers, replace the event model, supply keyboard semantics or repair native application lifecycle. No unsupported alternative route is proposed.
