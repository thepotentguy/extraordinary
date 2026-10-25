"""Reproduce the reviewed ZIPs from exact editable source; standard library only."""
from pathlib import Path
import zipfile,json,hashlib
root=Path(__file__).resolve().parent.parent
for b in json.loads((root/'source/brands.json').read_text()):
    p=root/'source/themes'/b['id']; names=json.loads((p/'directory-entries.json').read_text())
    files={n:b'' for n in names}
    files.update({str(f.relative_to(p)).replace('\\','/'):f.read_bytes() for f in p.rglob('*') if f.is_file() and f.name!='directory-entries.json'})
    dest=root/'packages'/(b['id']+'-Legacy-BookNow-R1.zip')
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in sorted(files.items()):
            info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,d)
    manifest=json.loads((root/'packages'/(b['id']+'-manifest.json')).read_text())
    actual=hashlib.sha256(dest.read_bytes()).hexdigest()
    if actual!=manifest['sha256']:raise SystemExit(b['id']+' differs: review and regenerate manifest before release')
    print(b['id']+': exact SHA-256 reproduced')
