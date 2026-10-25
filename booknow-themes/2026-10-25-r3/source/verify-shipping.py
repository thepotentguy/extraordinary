from pathlib import Path
from urllib.request import urlopen
import json,hashlib,zipfile,re
root=Path(__file__).resolve().parent.parent
rows=[];sha=lambda x:hashlib.sha256(x).hexdigest()
for b in json.loads((root/'source/brands.json').read_text(encoding='utf-8')):
 m=json.loads((root/'packages'/(b['id']+'-manifest.json')).read_text())
 assert sha((root/'packages'/m['file']).read_bytes())==m['sha256']
 with zipfile.ZipFile(root/'packages'/m['file']) as z:
  for name in ['mainStyle.css','mobile.css','theme.css','mobileTheme.css','brand-fonts.css']:
   member='black-rhino2021/css/'+name;expected=next(x['sha256'] for x in m['members'] if x['path']==member)
   response=urlopen('http://127.0.0.1:9145/package-css/'+b['id']+'/'+member).read()
   assert sha(z.read(member))==sha(response)==sha((root/'source/themes'/b['id']/member).read_bytes())==expected
   rows.append({'property':b['id'],'member':member,'zipSha256':m['sha256'],'memberSha256':expected,'zipSourceResponseEqual':True})
(root/'private-evidence/package-css-hashes.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Shipping proof: 25 served stylesheets match actual ZIP members and editable source, byte for byte.')
