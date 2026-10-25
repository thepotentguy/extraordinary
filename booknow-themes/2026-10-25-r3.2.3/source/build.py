from pathlib import Path
import zipfile,json,hashlib
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.2.2'
patch=(root/'source/mobile-details.css').read_bytes()
targets=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/mobileTheme.css']
sha=lambda b:hashlib.sha256(b).hexdigest()
(root/'packages').mkdir(parents=True,exist_ok=True)
release={'version':'R3.2.3','round':3,'date':'2026-10-25','status':'LOCAL candidate; actual native preview and publication pending.','scope':'Mobile detail tables open inside viewport with sticky native Close and internally scrollable content; desktop unchanged. Map data and native CMS parser remain unresolved. Prior mobileColor compatibility file retained unchanged, with live404 still unresolved.','patchSha256':sha(patch),'themes':[]}
for src in sorted((base/'packages').glob('*.zip')):
 brand=src.name.split('-Legacy-')[0]
 with zipfile.ZipFile(src) as z:members={n:z.read(n) for n in z.namelist()}
 for n in targets:members[n]+=patch
 out=root/'packages'/f'{brand}-Legacy-BookNow-R3.2.3.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in sorted(members.items()):
   i=zipfile.ZipInfo(n,(2026,10,25,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;z.writestr(i,b)
 with zipfile.ZipFile(src) as a,zipfile.ZipFile(out) as b:
  assert a.namelist()==b.namelist() and b.testzip() is None
  changed=[n for n in a.namelist() if a.read(n)!=b.read(n)]
  assert changed==targets
  assert all(b.read(n)==a.read(n)+patch for n in targets)
  record={'property':brand,'file':out.name,'sha256':sha(out.read_bytes()),'baseSha256':sha(src.read_bytes()),'files':132,'directories':8,'changedMembers':targets,'allOtherMembersUnchanged':True,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
 (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
 release['themes'].append({k:v for k,v in record.items() if k!='members'})
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8')
print(json.dumps(release,indent=2))
