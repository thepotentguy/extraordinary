from pathlib import Path
import json,zipfile,hashlib
root=Path(__file__).resolve().parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8'))
layouts=read(root/'private-evidence/layout-checks.json')['results'];native=read(root/'private-evidence/native-gallery-checks.json');align=read(root/'private-evidence/alignment-after.json');styles=read(root/'private-evidence/style-audit.json');shipping=read(root/'private-evidence/package-css-hashes.json');controls=read(root/'control-audit.json')
assert len(layouts)==205 and all(r['pass'] and not r.get('errors') for r in layouts)
assert len(native)==50 and all(r['pass'] for r in native)
assert all(r['aligned'] for r in align)
assert all(not r['nativeSelectorInlineRescueRules'] for r in styles)
assert len(shipping)==25 and all(r['zipSourceResponseEqual'] for r in shipping)
comparison=[]
for b in read(root/'source/brands.json'):
 old=root.parent/'2026-10-25-five-properties-r2/packages'/(b['id']+'-Legacy-BookNow-R2.zip');new=root/'packages'/(b['id']+'-Legacy-BookNow-R3.zip')
 with zipfile.ZipFile(old) as a,zipfile.ZipFile(new) as z:
  assert a.namelist()==z.namelist()
  changed=[n for n in a.namelist() if a.read(n)!=z.read(n)]
  assert changed==['black-rhino2021/css/mobileTheme.css','black-rhino2021/css/theme.css']
 comparison.append({'property':b['id'],'sha256':hashlib.sha256(new.read_bytes()).hexdigest(),'changedFromR2':changed,'unchangedFileMembers':129})
summary={'version':'R3','date':'2026-10-25','status':'Local correction/package candidate; independent and sponsor acceptance pending; no installation recommendation','authoredFixtureLayoutChecks':200,'authoredInteractionChecks':5,'nativeMouseRuntimeChecks':50,'alignmentRegressionWidths':5,'servedCssZipSourceHashChecks':25,'failures':0,'widths':[320,390,768,1024,1440],'phoneHeights':{'320':740,'390':844},'fixtureStates':['home','results','rates','noavailability','terms','photos','location','guest'],'alignment':[{'width':r['width'],'search':[r['search']['x'],r['search']['right']],'intro':[r['panel']['x'],r['panel']['right']],'hero':[r['main']['x'],r['main']['right']],'bookingGroupTops':[r[k]['y'] for k in ['date','occupancy','promo','cta']],'pass':r['aligned']} for r in align],'controls':controls,'packages':comparison,'previewCssAudit':styles,'stylesheetHashEvidence':shipping,'nativeKeyboard':'Not repaired: original runtime IMG/title/mouse controls have no demonstrated button/tab/key semantics. Authored keyboard fixture is separate.','openItems':['Native gallery keyboard and reduced-motion/autoplay behavior','Native Google Maps initialization','Native GWT dialog lifecycle/focus trap/escape','Property import/backup/rollback/public cache verification','Native validation/terms/gateway/payment/confirmation','Physical devices/soft keyboard and screen-reader tasks','Independent review and sponsor acceptance']}
(root/'verification-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
source=(root/'source/corrections.css').read_text().splitlines();needles=['#content .hotelImage img','#content .ratesText p','#content button:disabled','.gwt-DialogBox:has(#gallery) #formButtons button','#content #formDetails','#newsFeeds .newsFeedFlexTable']
with (root/'STYLE-AUDIT.md').open('w',encoding='utf-8') as f:
 f.write('# R3 shipped-style audit\n\nAll customer fixes are in source/corrections.css, compiled into both theme.css and mobileTheme.css in each archive. Later-screen inline CSS is restricted to review chrome and labelled placeholders.\n\n| Treatment / selector | Source line | Destination |\n|---|---:|---|\n')
 for n in needles:
  line=next(i+1 for i,s in enumerate(source) if n in s);f.write('| `'+n+'` | '+str(line)+' | `black-rhino2021/css/theme.css` and `mobileTheme.css` |\n')
 f.write('\nNative hidden states and original gallery inline geometry are preserved. Local pages load extracted ZIP assets; 25 ZIP/source/HTTP hashes match. Clean Git fixture links use byte-identical source members. See verification-summary.json and per-property member manifests.\n')
print('R3 final summary: 205 authored fixture + 50 native mouse cases passed; 5 alignment and 25 CSS hash checks; only two CSS members changed from R2.')
