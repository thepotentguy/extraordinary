from pathlib import Path
import json,shutil,re
root=Path(__file__).resolve().parent.parent
old=root.parent/'2026-10-25-five-properties-r3'
if not old.exists():old=root.parent/'2026-10-25-r3'
repair=root.parent/'2026-10-25-repair'
brands=json.loads((old/'source/brands.json').read_text(encoding='utf-8'))
(root/'source/brands.json').write_text(json.dumps(brands,indent=2)+'\n',encoding='utf-8',newline='\n')
shutil.copytree(old/'cms-assets',root/'cms-assets',dirs_exist_ok=True)
shutil.copytree(old/'previews/images',root/'previews/images',dirs_exist_ok=True)
shutil.copytree(old/'previews/runtime',root/'previews/runtime',dirs_exist_ok=True)
shutil.copy2(old/'previews/carousel.css',root/'previews/carousel.css')
native=(repair/'native-imbali-result.html').read_text(encoding='utf-8')
idle=(repair/'native-idle-dialog.html').read_text(encoding='utf-8')
steps=(root.parent/'2026-10-25-five-properties-r3.1/source/native-steps.html')
if not steps.exists():steps=root.parent/'2026-10-25-r3.1/source/native-steps.html'
steps=steps.read_text(encoding='utf-8')
for name,data in [('native-result.html',native),('native-idle.html',idle),('native-steps.html',steps)]:
 (root/'source'/name).write_text(data,encoding='utf-8',newline='\n')
script=(old/'source/fixture.js').read_text(encoding='utf-8')
script=script.replace("'location','guest']","'location','guest','idle']")
resultStart=script.index('const result=')
resultEnd=script.index('const photo=',resultStart)
script=script[:resultStart]+'''function nativeResult(noRates){
 const t=document.createElement('template');t.innerHTML=NATIVE_RESULT;
 const r=t.content.querySelector('.hotelResult');r.id='fixture-result';
 r.querySelector('h1').textContent=name;r.querySelector('h2').textContent='Native DOM replay: no live availability';
 r.querySelectorAll('a[href^="#PropertyDetail"]').forEach(a=>a.href='#fixture-property');
 r.querySelector('.hotelImage img').src=image;
 r.querySelectorAll('.hotelFeatures img').forEach(e=>e.src='../../package-css/'+id+'/black-rhino2021/images/features/'+e.src.split('/').pop());
 r.querySelector('.hotelDescription .gwt-HTML').textContent=document.body.dataset.description;
 const row=r.querySelector('.hotelNoRatesResult');
 row.querySelector('button').dataset.state='rates';
 if(!noRates){row.style.display='none';row.setAttribute('aria-hidden','true');const rates=r.querySelector('.hotelRates');rates.querySelectorAll('[aria-hidden]').forEach(e=>{e.removeAttribute('aria-hidden');e.style.removeProperty('display')});rates.querySelector('h4').textContent='Total stay';rates.querySelector('h5').textContent='Offline fixture';rates.querySelector('button').textContent='View Rates';rates.querySelector('button').dataset.state='rates';}
 r.querySelectorAll('.hotelInfo a').forEach(a=>a.dataset.state=a.classList.contains('pictureIcon')?'photos':'location');
 if(screen==='terms'||screen==='location'){r.querySelector('.hotelInfoContent').remove();r.insertAdjacentHTML('beforeend',detail(screen==='terms'?terms():locationPanel()));}
 return '<div class="hotelResults">'+r.outerHTML+'</div>';
}
const result=()=>nativeResult(false);
''' +script[resultEnd:]
start=script.index('const unavailable=');end=script.index('const guest=',start)
script=script[:start]+"const unavailable=()=>nativeResult(true);\n"+script[end:]
script=script.replace("screen==='noavailability'?unavailable()","(screen==='noavailability'||screen==='idle')?unavailable()")
script=script.replace("screen==='photos'?photo():''","screen==='photos'?photo():screen==='idle'?NATIVE_IDLE:''")
before="document.querySelectorAll('#bookingSteps .steps>div').forEach((e,i)=>e.className='stepsName'+(i+1)+(i===(isRates?1:0)?'':' unselected'));"
after="""const stage=Number(params.get('stage'))||(screen==='guest'?4:isRates?2:1);
 document.querySelectorAll('#bookingSteps .steps>div[class*="stepsName"]').forEach((e,i)=>{e.classList.toggle('unselected',i!==stage-1);e.firstElementChild.className=i===stage-1?'animated stepMoveInRight selected stepMoveInRight'+i:''});
 const back=document.querySelector('#bookingSteps .backButton');if(stage>1){back.removeAttribute('aria-hidden');back.style.removeProperty('display');back.dataset.state='results';}else{back.setAttribute('aria-hidden','true');back.style.display='none';}"""
assert before in script
script=script.replace(before,after)
script=script.replace(' role="button" tabindex="0"','')
script="const NATIVE_RESULT="+json.dumps(native)+";\nconst NATIVE_IDLE="+json.dumps(idle)+";\n"+script
script+="\ndocument.addEventListener('click',e=>{if(screen==='idle'&&e.target.matches('#photoMount #formButtons button')){document.querySelector('#photoMount').innerHTML='';}});\n"
(root/'source/fixture.js').write_text(script,encoding='utf-8',newline='\n')
for b in brands:
 p=root/'previews'/b['id'];p.mkdir(parents=True,exist_ok=True)
 html=(old/'previews'/b['id']/'journey.html').read_text(encoding='utf-8')
 html=html.replace('R3','R3.2')
 html=re.sub(r'<div id="bookingSteps">.*?(?=<div id="sideBar">)',steps,html,flags=re.S)
 html=html.replace('<nav aria-label="Offline review screens">','<nav aria-label="Offline review screens"><a href="?screen=idle" data-state="idle">Idle</a>')
 html=html.replace('Reconstructed layout fixture, not a native transaction.','Native Imbali result/idle and native step DOM replay with neutral property text. Other states retain native selector vocabulary with authored data. Not a native transaction.')
 (p/'journey.html').write_text(html,encoding='utf-8',newline='\n')
 home=(old/'previews'/b['id']/'home.html').read_text(encoding='utf-8').replace('R3','R3.2')
 (p/'home.html').write_text(home,encoding='utf-8',newline='\n')
print('Five R3.2 fixtures built; native result, idle and step DOM retained; no remote requests.')
