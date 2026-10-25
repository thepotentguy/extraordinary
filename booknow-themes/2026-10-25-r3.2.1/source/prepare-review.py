from pathlib import Path
import shutil,json
root=Path(__file__).resolve().parent.parent
base=root.parent/'2026-10-25-five-properties-r3.2'
if not base.exists():base=root.parent/'2026-10-25-r3.2'
brands=json.loads((base/'source/brands.json').read_text(encoding='utf-8'))
for name in ['fixture.js','brands.json','native-result.html','native-idle.html','native-steps.html']:
 (root/'source').mkdir(exist_ok=True);shutil.copy2(base/'source'/name,root/'source'/name)
shutil.copytree(base/'cms-assets',root/'cms-assets',dirs_exist_ok=True)
shutil.copytree(base/'previews/images',root/'previews/images',dirs_exist_ok=True)
for b in brands:
 p=root/'previews'/b['id'];p.mkdir(parents=True,exist_ok=True)
 html=(base/'previews'/b['id']/'journey.html').read_text(encoding='utf-8').replace('R3.2','R3.2.1')
 (p/'journey.html').write_text(html,encoding='utf-8',newline='\n')
print('Existing native-shaped R3.2 journey fixtures reused without nesting/class simplification.')
