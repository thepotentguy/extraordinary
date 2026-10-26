from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).resolve().parent.parent
H=R.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
bases={
 'mabula':(H/'2026-10-26-mabula-scroll-r3/packages/mabula-Legacy-BookNow-20261026-Scroll-R3.zip','1fe8779b64a467aeabf2025fd49153a908cd822bcd9be5dad48aecb54d48c9ad'),
 'safari-plains':(H/'2026-10-26-three-properties-r2/packages/safari-plains-Legacy-BookNow-20261026-R2.zip','3154d5b51011bac1a052e04b83582ec22a88053fea7553c5caa6a3b979227ddf'),
 'angels-view':(H/'2026-10-26-three-properties-r2/packages/angels-view-Legacy-BookNow-20261026-R2.zip','6b8a8225b566a7731e7fdaf1b0918788a497ee026107f821663fde6d870a6d9a')}
patch=(R/'source/native-panel-repair.css').read_bytes()
targets=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/theme.css','black-rhino2021/css/mobileTheme.css']
(R/'packages').mkdir(exist_ok=True)
releases=[]
for brand,(src,expected) in bases.items():
 assert sha(src.read_bytes())==expected
 with zipfile.ZipFile(src) as z:old={n:z.read(n) for n in z.namelist()}
 members=dict(old)
 for n in targets:members[n]+=b'\n'+patch
 out=R/'packages'/f'{brand}-Legacy-BookNow-20261026-Journey-R4.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in sorted(members.items()):
   i=zipfile.ZipInfo(n,(2026,10,26,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;z.writestr(i,b)
 with zipfile.ZipFile(out) as z:
  assert z.testzip() is None
  assert sorted(n for n in old if old[n]!=z.read(n))==sorted(targets)
  assert all(z.read(n)==old[n]+b'\n'+patch for n in targets)
  assert not any(n.endswith(('.html','.js','.exe')) for n in members)
 for n,b in members.items():
  p=R/'package-css'/brand/n
  if n.endswith('/'):p.mkdir(parents=True,exist_ok=True)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 record={'property':brand,'version':'20261026-Journey-R4','file':out.name,'sha256':sha(out.read_bytes()),'baseSha256':expected,'patchSha256':sha(patch),'changedMembers':targets,'allOtherMembersUnchanged':True,'files':sum(not n.endswith('/') for n in members),'directories':sum(n.endswith('/') for n in members),'members':[{'path':n,'sha256':sha(b)} for n,b in sorted(members.items()) if not n.endswith('/')]}
 (R/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
 releases.append({k:v for k,v in record.items() if k!='members'})
(R/'release-manifest.json').write_text(json.dumps({'date':'2026-10-26','status':'Deterministic build artifact; publication and acceptance are recorded separately in LIVE-VERIFICATION.md','themes':releases},indent=2),encoding='utf-8')
print(json.dumps(releases,indent=2))
