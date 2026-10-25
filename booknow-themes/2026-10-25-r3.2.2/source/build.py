from pathlib import Path
import zipfile,json,hashlib
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.2.1'
target='black-rhino2021/css/colourSchemes/mobileColor.css'
css=b'''/* Native mobile shell compatibility resource.
 * Shared colours are already loaded from colourSchemes/color.css.
 * Property-specific responsive styles remain in mobile.css and mobileTheme.css.
 * No duplicate colour rules: preserve the accepted R3.2.1 appearance.
 */
'''
sha=lambda b:hashlib.sha256(b).hexdigest()
(root/'packages').mkdir(parents=True,exist_ok=True)
(root/'source/mobileColor.css').write_bytes(css)
release={'version':'R3.2.2','date':'2026-10-25','round':3,'status':'LOCAL verified package candidate; native installation/public missing-resource confirmation pending.','scope':'One missing compatibility stylesheet added, with no style rules; all original members unchanged. Map data and native CMS parser limitation remain separate.','themes':[]}
for src in sorted((base/'packages').glob('*.zip')):
 brand=src.name.split('-Legacy-')[0]
 with zipfile.ZipFile(src) as z:members={n:z.read(n) for n in z.namelist()}
 assert target not in members
 members[target]=css
 out=root/'packages'/f'{brand}-Legacy-BookNow-R3.2.2.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,b in sorted(members.items()):
   info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,b)
 with zipfile.ZipFile(src) as a,zipfile.ZipFile(out) as b:
  assert b.testzip() is None and set(b.namelist())-set(a.namelist())=={target}
  assert all(a.read(n)==b.read(n) for n in a.namelist())
  assert sum(not n.endswith('/') for n in b.namelist())==132
  record={'property':brand,'file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'baseSha256':sha(src.read_bytes()),'files':132,'directories':8,'addedMember':target,'addedMemberSha256':sha(css),'originalMembersUnchanged':True,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
 (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
 release['themes'].append({k:v for k,v in record.items() if k!='members'})
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8')
print(json.dumps(release,indent=2))
