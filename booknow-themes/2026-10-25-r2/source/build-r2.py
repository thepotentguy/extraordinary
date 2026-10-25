from pathlib import Path
import json,zipfile,hashlib
root=Path(__file__).resolve().parent.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
layout=(root/'source/experience-layouts.css').read_text()
shared=layout.split('/* @property ')[0]
parts={s.split(' */',1)[0]:s.split(' */',1)[1] for s in layout.split('/* @property ')[1:]}
release={'date':'2026-10-25','version':'R2','status':'Consolidated creative revision; awaiting inspection; NOT installed','themes':[]}
for b in json.loads((root/'source/brands.json').read_text()):
    p=root/'source/themes'/b['id']
    for css in ['theme.css','mobileTheme.css']:
        f=p/'black-rhino2021/css'/css
        s=f.read_text().split('/* EXPERIENCE R2 */')[0].rstrip('\r\n')+'\n'
        f.write_text(s+'\n/* EXPERIENCE R2 */\n'+shared+parts[b['id']],encoding='utf-8',newline='\n')
    files={n:b'' for n in json.loads((p/'directory-entries.json').read_text())}
    files.update({str(f.relative_to(p)).replace('\\','/'):f.read_bytes() for f in p.rglob('*') if f.is_file() and f.name!='directory-entries.json'})
    out=root/'packages'/(b['id']+'-Legacy-BookNow-R2.zip')
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in sorted(files.items()):
            info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,d)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        assert sum(i.is_dir() for i in z.infolist())==8
        assert len([i for i in z.infolist() if not i.is_dir()])==131
        assert all(n.startswith('black-rhino2021/') for n in z.namelist())
        assert not any(n.endswith(('.js','.html')) for n in z.namelist())
    m={'property':b['id'],'version':'R2','file':out.name,'sha256':sha(out.read_bytes()),'bytes':len(out.read_bytes()),'files':131,'explicitDirectories':8,'javascriptIncluded':False,'htmlIncluded':False,'cmsAssetsSeparate':True,'status':'Awaiting sponsor review; no installation','members':[{'path':n,'sha256':sha(d)} for n,d in sorted(files.items()) if not n.endswith('/')]}
    (root/'packages'/(b['id']+'-manifest.json')).write_text(json.dumps(m,indent=2)+'\n')
    release['themes'].append({k:v for k,v in m.items() if k!='members'})
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n')
print('Five R2 ZIPs built; 131 files and eight directories each; no HTML/JS.')
