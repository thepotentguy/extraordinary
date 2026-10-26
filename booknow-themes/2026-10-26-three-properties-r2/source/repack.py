from pathlib import Path
import zipfile,hashlib,json
r=Path(__file__).resolve().parent.parent
rows=[]
for d in sorted((r/'package-css').iterdir()):
 if not d.is_dir():continue
 out=r/'packages'/(d.name+'-Legacy-BookNow-20261026-R2.zip')
 manifest=json.loads((r/'packages'/(d.name+'-manifest.json')).read_text())
 members={x['path']:(d/x['path']).read_bytes() for x in manifest['members']}
 dirs=set()
 for n in members:
  for parent in Path(n).parents:
   if str(parent)!='.':dirs.add(str(parent).replace(chr(92),'/')+'/')
 # Include the retained eight explicit native directory entries from existing package.
 with zipfile.ZipFile(out) as old:explicit=[n for n in old.namelist() if n.endswith('/')]
 for n in explicit:members[n]=b''
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for n,data in sorted(members.items()):
   info=zipfile.ZipInfo(n,(2026,10,26,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)
 digest=hashlib.sha256(out.read_bytes()).hexdigest()
 assert digest==manifest['sha256'],(d.name,'Source changed; regenerate and review package/member manifests before release')
 rows.append({'property':d.name,'sha256':digest})
print(json.dumps(rows,indent=2))
