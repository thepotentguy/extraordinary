from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).resolve().parent.parent;B=R.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
patch=(R/'source/gallery-return.css').read_bytes()
targets=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/theme.css','black-rhino2021/css/mobileTheme.css']
(R/'packages').mkdir(parents=True,exist_ok=True);records=[]
for brand in ['mabula','safari-plains','angels-view']:
 manifest=json.loads((B/'packages'/f'{brand}-manifest.json').read_text(encoding='utf-8'))
 base=B/'packages'/manifest['file'];assert sha(base.read_bytes())==manifest['sha256']
 with zipfile.ZipFile(base) as z:old={n:z.read(n) for n in z.namelist()}
 new=dict(old)
 for n in targets:new[n]+=b'\n'+patch
 out=R/'packages'/f'{brand}-Legacy-BookNow-20261026-UX-R5.1.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in sorted(new.items()):
   i=zipfile.ZipInfo(n,(2026,10,26,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;z.writestr(i,b)
 with zipfile.ZipFile(out) as z:assert z.testzip() is None;assert sorted(n for n in old if old[n]!=z.read(n))==sorted(targets)
 for n,b in new.items():
  p=R/'package-css'/brand/n
  if n.endswith('/'):p.mkdir(parents=True,exist_ok=True)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 record={'property':brand,'file':out.name,'sha256':sha(out.read_bytes()),'baseSha256':manifest['sha256'],'patchSha256':sha(patch),'changedMembers':targets,'allOtherMembersUnchanged':True,'members':[{'path':n,'sha256':sha(b)} for n,b in sorted(new.items()) if not n.endswith('/')]}
 (R/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2),encoding='utf-8');records.append({k:v for k,v in record.items() if k!='members'})
(R/'release-manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8');print(json.dumps(records))
