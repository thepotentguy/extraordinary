from pathlib import Path
import json,zipfile,hashlib,re
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.1'
if not base.exists(): base=root.parent/'2026-10-25-r3.1'
sha=lambda b:hashlib.sha256(b).hexdigest()
oldcopy=b'Shared legacy photographs';newcopy=b'Photo gallery'
expected=['black-rhino2021/css/mainStyle.css','black-rhino2021/css/mobileTheme.css','black-rhino2021/css/theme.css']
(root/'packages').mkdir(exist_ok=True)
release={'version':'R3.1.1','date':'2026-10-25','scope':'Caption copy only; not installed by design chat','themes':[]}
audit={'scope':'Every CSS member in all five shipping ZIPs; CSS content declarations, including literal text and nonliteral value categories. No application JS/CMS/private content reviewed.','inventory':[],'findings':[],'checks':[]}
for old in sorted((base/'packages').glob('*-Legacy-BookNow-R3.1.zip')):
    brand=old.name.split('-Legacy-')[0]
    with zipfile.ZipFile(old) as z: members={n:z.read(n) for n in z.namelist()}
    fixes=[]
    for n,data in list(members.items()):
        if n.endswith('.css') and oldcopy in data:
            fixes.append({'path':n,'replacements':data.count(oldcopy)})
            members[n]=data.replace(oldcopy,newcopy)
    assert sorted(x['path'] for x in fixes)==expected,(brand,fixes)
    assert all(x['replacements']==1 for x in fixes)
    out=root/'packages'/f'{brand}-Legacy-BookNow-R3.1.1.zip'
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,data in sorted(members.items()):
            info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data)
    with zipfile.ZipFile(old) as a,zipfile.ZipFile(out) as b:
        assert a.namelist()==b.namelist() and b.testzip() is None
        differences=[n for n in a.namelist() if a.read(n)!=b.read(n)]
        assert differences==expected
        assert sum(not n.endswith('/') for n in b.namelist())==131
        assert sum(n.endswith('/') for n in b.namelist())==8
        assert not any(n.endswith(('.html','.js')) for n in b.namelist())
        for n in differences: assert a.read(n).replace(oldcopy,newcopy)==b.read(n)
        # Preserve the entire mobile steps correction appended in R3.1.
        assert a.read(expected[1]).split(b'/* R3.1:')[1]==b.read(expected[1]).split(b'/* R3.1:')[1]
        record={'property':brand,'version':'R3.1.1','file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'files':131,'explicitDirectories':8,'copyReplacements':fixes,'changedMembers':differences,'onlyCaptionStringChanged':True,'members':[{'path':n,'sha256':sha(b.read(n))} for n in b.namelist() if not n.endswith('/')]}
    (root/'packages'/f'{brand}-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    release['themes'].append({k:v for k,v in record.items() if k!='members'})
    count=0
    for n,data in members.items():
        if not n.endswith('.css'): continue
        count+=1;text=data.decode('utf-8-sig')
        for rule in re.finditer(r'([^{}]+)\{([^{}]*)\}',text):
            for prop in re.finditer(r'(?:^|;)\s*content\s*:\s*((?:"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|[^;}])+)',rule[2]):
                value=prop[1].strip();literal=value.startswith(('"',"'"))
                row={'property':brand,'path':n,'selector':rule[1].strip(),'value':value if literal else ('url(...)' if value.startswith('url(') else value),'literal':literal}
                audit['inventory'].append(row)
                if literal and re.search(r'\b(?:shared|legacy|clifftop|fixture|prototype|placeholder|synthetic|offline|demo|internal)\b|not loaded',value,re.I):audit['findings'].append(row)
    audit['checks'].append({'property':brand,'cssFilesReviewed':count,'copyReplacements':len(fixes),'otherFilesUnchanged':128,'r31StepsSuffixIdentical':True})
assert len(release['themes'])==5
assert not audit['findings'],audit['findings']
(root/'release-manifest.json').write_text(json.dumps(release,indent=2)+'\n',encoding='utf-8',newline='\n')
(root/'content-audit.json').write_text(json.dumps(audit,indent=2)+'\n',encoding='utf-8',newline='\n')
literalValues=sorted(set(x['value'] for x in audit['inventory'] if x['literal']))
print(json.dumps({'packages':len(release['themes']),'checks':audit['checks'],'findings':audit['findings'],'literalValues':literalValues}))
