from pathlib import Path
from urllib.request import Request, urlopen
import json,re,hashlib

root=Path(__file__).resolve().parent.parent
brands=json.loads((root/'source/brands.json').read_text())
def fetch(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:return r.read()
sources=[]
for b in brands:
    p=root/'source/assets'/b['id']; p.mkdir(parents=True,exist_ok=True)
    for role in ['logo','hero']:
        name=role+('.png' if role=='logo' else '.jpg'); target=p/name
        if not target.exists():target.write_bytes(fetch(b[role]))
        sources.append({'property':b['id'],'role':role,'url':b[role],'file':str(target.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'observed':'2026-10-25','rights':'Existing official property website asset; property-owned use only. No third-party redistribution licence asserted.'})
fontdir=root/'source/fonts';fontdir.mkdir(exist_ok=True)
families={b['headingFont'] for b in brands}|{b['bodyFont'] for b in brands}
for family in sorted(families):
    slug=family.lower().replace(' ','');cssfile=fontdir/(slug+'.css')
    if cssfile.exists():continue
    css=fetch('https://fonts.googleapis.com/css2?family='+family.replace(' ','+')+':wght@400;500;600;700&display=swap').decode()
    # The non-browser response supplies complete Latin-compatible TTF faces.
    urls=list(dict.fromkeys(re.findall(r'url\((https:[^)]+)\)',css)))
    for i,url in enumerate(urls):
        name=slug+'-'+str(i)+('.woff2' if '.woff2' in url else '.ttf')
        data=fetch(url);(fontdir/name).write_bytes(data);css=css.replace(url,name)
    cssfile.write_text(css)
    licence=fetch('https://raw.githubusercontent.com/google/fonts/main/ofl/'+slug+'/OFL.txt')
    (fontdir/(slug+'-OFL.txt')).write_bytes(licence)
(root/'source/asset-sources.json').write_text(json.dumps(sources,indent=2)+'\n')
print('Bounded collection complete: 5 authentic marks, 5 property images, 7 font families; no crawl.')
