# Editable source and reproducibility

package-css/ is the complete editable shipping source, with exact per-member hashes in packages/*-manifest.json. source/*.css contains the authored identity and shared safety layers for review; embedded font data and retained native styles are present in the complete shipping CSS.

Run `python source/repack.py` to rebuild the three unchanged ZIPs byte-for-byte from package-css/ and verify their recorded hashes. Edited shipping sources need regenerated manifests, testing and review. Editing an explanatory CSS layer alone does not update shipping CSS automatically.

The gallery-bound authoring script, raw originals and private source records remain in the owner's private project lane. Room-review-only images are provided privately; exact room bindings stay on HOLD. No private runtime or credentials are required to inspect or repack the themes.

Font sources: Bodoni Moda, Inria Serif and Plus Jakarta Sans downloaded from the official google/fonts OFL directories on 26 October 2026; Poppins reused from the accepted 25 October local source with original OFL. Exact retained font bytes have their own hashes in FONT-SOURCES.json. Licences are retained; logos keep their original lettering.

Offline home previews retain the previously captured public native gallery runtime byte-for-byte, including its original pace/events. Only this local proof includes that runtime; no JavaScript or HTML is shipped in a theme ZIP. Journey transitions are authored offline fixture handlers and cannot establish native booking behaviour. CSS reduced-motion rules do not modify JavaScript carousel autoplay or add missing keyboard events.
