from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json,re,zipfile,hashlib,base64,shutil,sys,io,colorsys,html

ROOT=Path(__file__).resolve().parent.parent
BASE=ROOT.parent/'2026-10-16/iterations/2026-10-23-R4.2/Clifftop-Native-R4.2-Complete-Theme.zip'
EXPECTED='2d4e519f21ca9ec64866a85303a3c177e42cc378c396e536fe2729632e43406e'
sha=lambda d:hashlib.sha256(d).hexdigest()
brands=json.loads((ROOT/'source/brands.json').read_text())
chosen=sys.argv[1:]
if chosen:brands=[b for b in brands if b['id'] in chosen]
layout=(ROOT/'source/property-layouts.css').read_text()
shared=layout.split('/* @property ')[0]
pieces={x.split(' */',1)[0]:x.split(' */',1)[1] for x in layout.split('/* @property ')[1:]}

def fontcss(b):
    out=''
    for family in [b['headingFont'],b['bodyFont']]:
        slug=family.lower().replace(' ','')
        css=(ROOT/'source/fonts'/(slug+'.css')).read_text()
        for name in re.findall(r'url\(([^)]+)\)',css):
            raw=(ROOT/'source/fonts'/name).read_bytes(); mime='font/woff2' if name.endswith('woff2') else 'font/ttf'
            css=css.replace(name,'data:'+mime+';base64,'+base64.b64encode(raw).decode())
        out+=css+'\n'
    return out.encode()

def recolor(text,b):
    text=text.replace('--clifftop','--brand').replace('Clifftop','Shared legacy').replace('clifftop','brand')
    text=text.replace('EB Garamond',b['headingFont']).replace('Poppins',b['bodyFont'])
    h,s,v=colorsys.rgb_to_hsv(*[int(b['ink'][i:i+2],16)/255 for i in (1,3,5)])
    def col(m):
        old=m.group(0); raw=old[1:7]
        if len(raw)!=6:return old
        rgb=[int(raw[i:i+2],16)/255 for i in (0,2,4)]
        oh,os,ov=colorsys.rgb_to_hsv(*rgb)
        # Replace inherited ochre/brown palette, preserving tonal hierarchy.
        if .04<=oh<=.16 and os>.07:
            new=colorsys.hsv_to_rgb(h,min(.64,os*(.7+s*.5)),ov)
            return '#'+''.join(f'{round(x*255):02x}' for x in new)+old[7:]
        return old
    text=re.sub(r'#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?\b',col,text)
    text=re.sub(r':root\{--brand-ink:[^}]+\}',':root{--brand-ink:'+b['ink']+';--brand-accent:'+b['accent']+';--brand-surface:'+b['surface']+';--brand-edge:'+b['edge']+";--brand-body:'"+b['bodyFont']+"',Arial,sans-serif;--brand-heading:'"+b['headingFont']+"',serif}",text)
    return text

def assets(b):
    p=ROOT/'source/assets'/b['id']; q=ROOT/'cms-assets'/b['id'];q.mkdir(parents=True,exist_ok=True)
    im=Image.open(p/'logo.png').convert('RGBA');bbox=im.getbbox();im=im.crop(bbox)
    im.save(q/'logo-full-colour.png')
    canvas=Image.new('RGBA',(230,100),(255,255,255,0));small=ImageOps.contain(im,(220,92),Image.Resampling.LANCZOS);canvas.alpha_composite(small,((230-small.width)//2,(100-small.height)//2));canvas.save(q/'logo-230x100.png')
    hero=Image.open(p/'hero.jpg').convert('RGB'); ImageOps.fit(hero,(670,300),method=Image.Resampling.LANCZOS).save(q/'carousel-01-670x300.jpg',quality=92)
    # A second crop of the same approved source demonstrates the native carousel.
    # It is labelled as an alternate crop, not additional photographic coverage.
    ImageOps.fit(hero,(670,300),method=Image.Resampling.LANCZOS,centering=(.5,.3)).save(q/'carousel-01-alt-crop-670x300.jpg',quality=92)
    ImageOps.fit(hero,(133,99),method=Image.Resampling.LANCZOS).save(q/'property-133x99.jpg',quality=92)
    return q

manifests=[]
for b in brands:
    cms=assets(b); target=ROOT/'source/themes'/b['id']; target.mkdir(parents=True,exist_ok=True)
    if BASE.exists():
        assert sha(BASE.read_bytes())==EXPECTED
        with zipfile.ZipFile(BASE) as z:
            original=z.infolist(); files={i.filename:z.read(i) for i in original}
        files={n:d for n,d in files.items() if '/licenses/' not in n or n.endswith('/')}
        for n,d in list(files.items()):
            if n.endswith('.css') and not n.endswith('brand-fonts.css'):files[n]=recolor(d.decode('utf-8-sig'),b).encode()
        files['black-rhino2021/css/brand-fonts.css']=fontcss(b)
        files['black-rhino2021/images/colourSchemes/custom/logo.png']=(cms/'logo-230x100.png').read_bytes()
        for licence in b['fontLicenseIds']:files['black-rhino2021/licenses/'+licence+'-OFL.txt']=(ROOT/'source/fonts'/(licence+'-OFL.txt')).read_bytes()
        addition='\n/* Property identity R1; native runtime unchanged. */\n'+shared+pieces[b['id']]
        files['black-rhino2021/css/theme.css']+=addition.encode()
        # mobile.html loads mobileTheme.css rather than theme.css. Mirror the
        # identity layer at the end so both native entry points receive it.
        files['black-rhino2021/css/mobileTheme.css']+=addition.encode()
        for n,d in files.items():
            dest=target/n
            if n.endswith('/'):dest.mkdir(parents=True,exist_ok=True)
            else:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(d)
        (target/'directory-entries.json').write_text(json.dumps([n for n in files if n.endswith('/')],indent=2))
    else:
        files={str(p.relative_to(target)).replace('\\','/'):p.read_bytes() for p in target.rglob('*') if p.is_file() and p.name!='directory-entries.json'}
        for n in json.loads((target/'directory-entries.json').read_text()):files[n]=b''
    out=ROOT/'packages'/(b['id']+'-Legacy-BookNow-R1.zip');out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in sorted(files.items()):
            info=zipfile.ZipInfo(n,(2026,10,25,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,d)
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        assert all(n.startswith('black-rhino2021/') for n in z.namelist())
        assert not any(n.endswith(('.js','.html')) for n in z.namelist())
        assert sum(i.is_dir() for i in z.infolist())==8
    manifest={'property':b['id'],'version':'R1','date':'2026-10-25','status':'Design review candidate; NOT installed','file':out.name,'sha256':sha(out.read_bytes()),'bytes':out.stat().st_size,'files':sum(not n.endswith('/') for n in files),'explicitDirectories':8,'baselineSha256':EXPECTED,'javascriptIncluded':False,'cmsAssetsSeparate':True,'nativeSelectorsVerified':'Read-only property-specific public home DOM on 25 October','sponsorAcceptance':'pending','members':[{'path':n,'sha256':sha(d)} for n,d in sorted(files.items()) if not n.endswith('/')]}
    (ROOT/'packages'/(b['id']+'-manifest.json')).write_text(json.dumps(manifest,indent=2)+'\n');manifests.append(manifest)
    print(b['id'],manifest['sha256'],manifest['files'],'files / 8 directories')

# Produce an authentic asset review sheet before accepting imagery/crops.
sheet=Image.new('RGB',(1200,320*len(brands)), '#ebe9e2');draw=ImageDraw.Draw(sheet)
for i,b in enumerate(brands):
    p=ROOT/'source/assets'/b['id']; im=Image.open(p/'logo.png').convert('RGBA');im=ImageOps.contain(im,(300,150));sheet.paste(im,(30,i*320+60),im)
    pic=ImageOps.contain(Image.open(p/'hero.jpg').convert('RGB'),(760,270));sheet.paste(pic,(390,i*320+25));draw.text((30,i*320+18),b['name'],fill='black')
sheet.save(ROOT/'previews'/('asset-review-'+('-'.join(chosen) if chosen else 'all')+'.jpg'),quality=90)
