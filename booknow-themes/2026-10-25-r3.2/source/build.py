from pathlib import Path
import json,zipfile,hashlib,sys
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.1.1'
if not base.exists():base=root.parent/'2026-10-25-r3.1.1'
patch=(root/'source/round1.css').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
changed=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/mobileTheme.css','black-rhino2021/css/theme.css']
release={'date':'2026-10-25','version':'R3.2','round':1,'status':'Local repair evidence; origin native review pending; not installed by design chat','themes':[]}
(root/'packages').mkdir(exist_ok=True)
for old in sorted((base/'packages').glob('*-Legacy-BookNow-R3.1.1.zip')):
 brand=old.name.split('-Legacy-')[0]
 with zipfile.ZipFile(old) as z:members={n:z.read(n) for n in z.namelist()}
 for n in changed:members[n]+=b'\n'+patch
 out=root/'packages'/f'{brand}-Legacy-BookNow-R3.2.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,data in sorted(members.items()):
   info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)
 with zipfile.ZipFile(old) as a,zipfile.ZipFile(out) as b:
  assert a.namelist()==b.namelist() and b.testzip() is None
  differences=[n for n in a.namelist() if a.read(n)!=b.read(n)]
  assert differences==changed
  assert sum(not n.endswith('/') for n in b.namelist())==131
  assert not any(n.endswith(('.js','.html')) for n in b.namelist())
  for n in changed:assert b.read(n)==a.read(n)+b'\n'+patch
  if '--extract-for-review' in sys.argv:b.extractall(root/'package-css'/brand)
  manifest={'property':brand,'version':'R3.2','file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'files':131,'directories':8,'changedMembers':changed,'unchangedMembers':128,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
 (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
 release['themes'].append({k:v for k,v in manifest.items() if k!='members'})
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'packages':len(release['themes']),'changedCssPerProperty':3,'otherFilesUnchanged':640,'patchSha256':sha(patch)}))
