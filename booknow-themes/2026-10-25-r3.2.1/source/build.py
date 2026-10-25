from pathlib import Path
import json,zipfile,hashlib,sys
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.2'
if not base.exists():base=root.parent/'2026-10-25-r3.2'
patch=(root/'source/button-margins.css').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
changed=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/mobileTheme.css','black-rhino2021/css/theme.css']
(root/'packages').mkdir(exist_ok=True)
release={'version':'R3.2.1','date':'2026-10-25','round':2,'status':'Minimal button-margin follow-up; native acceptance pending; no installation by design chat','themes':[]}
audit={'scope':'Margin declarations on the four native recovery/rate button classes in all shipping CSS members. Positive, auto and negative legacy values retained in audit; shipping override resets their scoped margins only.','properties':[]}
import re
for old in sorted((base/'packages').glob('*-Legacy-BookNow-R3.2.zip')):
 brand=old.name.split('-Legacy-')[0]
 with zipfile.ZipFile(old) as z:members={n:z.read(n) for n in z.namelist()}
 findings=[]
 for n,data in members.items():
  if not n.endswith('.css'):continue
  for rule in re.finditer(r'([^{}]+)\{([^{}]*)\}',data.decode('utf-8-sig')):
   if re.search(r'\.(?:viewAlternativeDatesLink|viewRatesLink|smallButton|standardButton)\b',rule[1]):
    for margin in re.finditer(r'(?:^|;)\s*(margin(?:-(?:left|right|top|bottom))?)\s*:\s*([^;}]+)',rule[2]):findings.append({'file':n,'selector':rule[1].strip(),'property':margin[1],'value':margin[2].strip()})
 audit['properties'].append({'property':brand,'matches':findings})
 for n in changed:members[n]+=b'\n'+patch
 out=root/'packages'/f'{brand}-Legacy-BookNow-R3.2.1.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,data in sorted(members.items()):
   info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)
 with zipfile.ZipFile(old) as a,zipfile.ZipFile(out) as b:
  assert a.namelist()==b.namelist() and b.testzip() is None
  assert [n for n in a.namelist() if a.read(n)!=b.read(n)]==changed
  assert sum(not n.endswith('/') for n in b.namelist())==131
  assert sum(n.endswith('/') for n in b.namelist())==8
  assert not any(n.endswith(('.html','.js')) for n in b.namelist())
  for n in changed:assert b.read(n)==a.read(n)+b'\n'+patch
  if '--extract-for-review' in sys.argv:b.extractall(root/'package-css'/brand)
  manifest={'property':brand,'version':'R3.2.1','file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'files':131,'directories':8,'changedMembers':changed,'unchangedFiles':128,'preservedR32Prefix':True,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
 (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
 release['themes'].append({k:v for k,v in manifest.items() if k!='members'})
assert len(release['themes'])==5
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8',newline='\n')
(root/'button-margin-audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'themes':5,'changedCssPerTheme':3,'unchangedFiles':640,'patchSha256':sha(patch),'auditMatches':sum(len(x['matches']) for x in audit['properties'])}))
