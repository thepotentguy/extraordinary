from pathlib import Path
import json,hashlib,shutil,zipfile
root=Path(__file__).resolve().parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=root/'verification-before-tablet-dialog-fix.json'
if not before.exists():shutil.copy2(root/'verification.json',before)
full=json.loads(before.read_text(encoding='utf-8'))
idle=json.loads((root/'verification-idle.json').read_text(encoding='utf-8'))
full['checks']=[x for x in full['checks'] if x['state']!='idle']+idle['checks']
full['shipping']=idle['shipping']
full['finalRetest']='The final shipping change only alters non-gallery dialog width to fit-content. All 30 affected idle cases were rerun and passed; prior five tablet failures retained in verification-before-tablet-dialog-fix.json. Other 240 layouts, 120 step states, ten local transition/keyboard checks and 12 original-PNG geometry checks are retained from the preceding full run; their selectors are unaffected by this scoped change.'
assert len(full['checks'])==270 and all(x['pass'] for x in full['checks'])
assert all(x['pass'] for x in full['transitions']) and all(x['pass'] for x in full['transparentLogos'])
release=json.loads((root/'release-manifest.json').read_text(encoding='utf-8'))
for t in release['themes']:
 p=root/'packages'/t['file'];assert sha(p)==t['sha256']
 with zipfile.ZipFile(p) as z:
  for x in [s for s in full['shipping'] if s['property']==t['property']]:assert hashlib.sha256(z.read('black-rhino2021/css/'+x['file'])).hexdigest()==x['hash']
(root/'verification.json').write_text(json.dumps(full,indent=2)+'\n',encoding='utf-8',newline='\n')
summary={'version':'R3.2','round':1,'layoutCases':270,'layoutFailures':0,'nativeShapeStepPermutations':120,'localRecoveryAndKeyboardChecks':10,'previewOnlyOriginalPngChecks':12,'shippingCssHashes':15,'targetedFinalIdleRetest':30,'priorFailuresPreserved':before.name,'status':'Frozen review candidate; origin native acceptance pending. No installation by design chat.','sourceHashes':{n:sha(root/'source'/n) for n in ['round1.css','check-round1.cjs','build.py','prepare-fixtures.py','baseline.cjs','capture-stable-homes.cjs']},'archiveHashes':{t['property']:t['sha256'] for t in release['themes']},'limits':['No new availability searches by design chat.','Home source frames capped670x300; property thumbnails capped133x99; no new raster assets shipped.','Local state/keyboard/layout evidence is not native application, touchscreen, accessibility or complete checkout certification.','CMS cropper0x0 blocks original PNG/carousel asset updates; no bypass.','Native missing map/gallery data and missing mobileColor.css remain separate.','Canonical task identity/destination unavailable; local evidence retained and canonical update pending.']}
(root/'verification-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['limits','sourceHashes','archiveHashes']}))
