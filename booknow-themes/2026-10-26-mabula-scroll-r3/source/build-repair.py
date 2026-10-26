from pathlib import Path
import hashlib,json,zipfile,shutil
R=Path(__file__).resolve().parent.parent
BASE=R.parent/'2026-10-26-three-properties-r2'
EXPECTED='dd32677fda045e8a69891a659e40e54b0f11d3b5a0ef70b22b602411dfc966a2'
sha=lambda b:hashlib.sha256(b).hexdigest()
src=BASE/'packages/mabula-Legacy-BookNow-20261026-R2.zip'
assert sha(src.read_bytes())==EXPECTED
patch=(R/'source/mabula-home-scroll.css').read_bytes()
targets=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/theme.css','black-rhino2021/css/mobileTheme.css']
with zipfile.ZipFile(src) as z: original={n:z.read(n) for n in z.namelist()}
members=dict(original)
for n in targets:members[n]+=b'\n'+patch
out=R/'packages/mabula-Legacy-BookNow-20261026-Scroll-R3.zip';out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n,b in sorted(members.items()):
  i=zipfile.ZipInfo(n,(2026,10,26,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;z.writestr(i,b)
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert set(z.namelist())==set(original)
 assert sorted(n for n in original if original[n]!=z.read(n))==sorted(targets)
 assert all(z.read(n)==original[n]+b'\n'+patch for n in targets)
 assert not any(n.endswith(('.html','.js','.exe')) for n in members)
 for n,b in members.items():
  p=R/'package-css/mabula'/n
  if n.endswith('/'):p.mkdir(parents=True,exist_ok=True)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
manifest={'property':'mabula','version':'20261026-Scroll-R3','file':out.name,'sha256':sha(out.read_bytes()),'baseSha256':EXPECTED,'patchSha256':sha(patch),'changedMembers':targets,'files':sum(not n.endswith('/') for n in members),'directories':sum(n.endswith('/') for n in members),'allOtherMembersUnchanged':True,'members':[{'path':n,'sha256':sha(b)} for n,b in sorted(members.items()) if not n.endswith('/')]}
(R/'packages/mabula-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(R/'release-manifest.json').write_text(json.dumps({k:v for k,v in manifest.items() if k!='members'},indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in manifest.items() if k!='members'},indent=2))
