from pathlib import Path
import zipfile,json,hashlib
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3'
if not base.exists(): base=root.parent/'2026-10-25-r3'
sha=lambda b:hashlib.sha256(b).hexdigest()
patch=(root/'source/mobile-steps.css').read_bytes()
release={'version':'R3.1','date':'2026-10-25','scope':'Mobile steps only; native input acceptance pending; not installed','themes':[]}
(root/'packages').mkdir(exist_ok=True)
for old in sorted((base/'packages').glob('*-Legacy-BookNow-R3.zip')):
    brand=old.name.split('-Legacy-')[0]
    with zipfile.ZipFile(old) as z: members={n:z.read(n) for n in z.namelist()}
    changed='black-rhino2021/css/mobileTheme.css'
    members[changed]+=b'\n'+patch
    out=root/'packages'/f'{brand}-Legacy-BookNow-R3.1.zip'
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,data in sorted(members.items()):
            info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,data)
    with zipfile.ZipFile(old) as a,zipfile.ZipFile(out) as b:
        assert a.namelist()==b.namelist() and b.testzip() is None
        differences=[n for n in a.namelist() if a.read(n)!=b.read(n)]
        assert differences==[changed]
        assert sum(not n.endswith('/') for n in b.namelist())==131
        assert sum(n.endswith('/') for n in b.namelist())==8
        assert not any(n.endswith(('.js','.html')) for n in b.namelist())
        record={'property':brand,'version':'R3.1','file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'files':131,'explicitDirectories':8,'changedMembers':differences,'desktopThemeUnchanged':True,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
    (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    release['themes'].append({k:v for k,v in record.items() if k!='members'})
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'packages':len(release['themes']),'changedMember':changed,'desktopBytes':'identical to R3'}))
