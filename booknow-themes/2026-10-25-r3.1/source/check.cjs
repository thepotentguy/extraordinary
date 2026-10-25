const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
const base=path.resolve(root,fs.existsSync(path.resolve(root,'../2026-10-25-five-properties-r3'))?'../2026-10-25-five-properties-r3':'../2026-10-25-r3');
const brands=JSON.parse(fs.readFileSync(path.join(base,'source/brands.json'),'utf8'));
const native=fs.readFileSync(path.join(__dirname,'native-steps.html'),'utf8');
const patch=fs.readFileSync(path.join(__dirname,'mobile-steps.css'),'utf8');
const measure=()=>{const visible=e=>e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0;
 const box=e=>{let r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom}};
 return {height:document.querySelector('#bookingSteps').getBoundingClientRect().height,
 labels:[...document.querySelectorAll('#bookingSteps .steps a')].filter(visible).map(e=>({text:e.textContent,...box(e)})),
 inactive:[...document.querySelectorAll('#bookingSteps .steps>.unselected')].filter(visible).length,
 dividers:[...document.querySelectorAll('#bookingSteps .steps>.gwt-Label')].filter(visible).length,
 hidden:[...document.querySelectorAll('#bookingSteps [aria-hidden=true]')].filter(visible).length,
 actions:[...document.querySelectorAll('#bookingSteps>div>a')].filter(visible).map(e=>({text:e.textContent,...box(e)})),
 width:innerWidth,scrollWidth:document.documentElement.scrollWidth};};
(async()=>{let browser=await chromium.launch({channel:'chrome',headless:true}),page=await browser.newPage(),rows=[],baseline=[];
 for(const b of brands){for(const w of [320,390,768]){
  await page.setViewportSize({width:w,height:1000});
  // Only local authored replay; no native app/backend or availability request.
  await page.goto('http://127.0.0.1:9145/previews/'+b.id+'/journey.html?screen=results');
  await page.evaluate(html=>{document.body.innerHTML='<div id="contentWrapper">'+html+'<div id="content"><p>Native steps DOM replay only</p></div></div>';},native);
  await page.evaluate(()=>document.fonts.ready);
  baseline.push({property:b.id,width:w,...await page.evaluate(measure)});
  await page.addStyleTag({content:patch});
  for(let step=1;step<=4;step++){for(const action of ['none','back','forward']){
   await page.evaluate(({step,action})=>{
    document.querySelectorAll('#bookingSteps .steps>div[class*=stepsName]').forEach((e,i)=>e.classList.toggle('unselected',i!==step-1));
    document.querySelectorAll('#bookingSteps>div>a').forEach(e=>{e.setAttribute('aria-hidden','true');e.style.display='none'});
    const target=action==='back'?'.backButton':action==='forward'?'.forwardButtonWide':null;
    if(target){let e=document.querySelector('#bookingSteps '+target);e.removeAttribute('aria-hidden');e.style.removeProperty('display')}
   },{step,action});
   const m=await page.evaluate(measure),expect=['Hotels','Rates','Services','Details'][step-1];
   const all=[...m.labels,...m.actions];
   const overlap=all.some((a,i)=>all.some((b,j)=>j>i&&Math.min(a.right,b.right)-Math.max(a.x,b.x)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>1));
   const pass=m.labels.length===1&&m.labels[0].text===expect&&m.inactive===0&&m.dividers===0&&m.hidden===0&&m.actions.length===(action==='none'?0:1)&&all.every(x=>x.height>=44&&x.x>=0&&x.right<=w+1)&&!overlap&&m.scrollWidth<=w;
   rows.push({property:b.id,width:w,step,action,pass,overlap,...m});
   if(b.id==='kingfisher'&&step===1&&action==='none')await page.screenshot({path:path.join(root,'previews',`kingfisher-steps-${w}.png`)});
  }}
 }}
 // The mobile correction does not match desktop widths. Check computed state equality.
 const desktop=[];
 for(const b of brands){await page.setViewportSize({width:1440,height:1000});await page.goto('http://127.0.0.1:9145/previews/'+b.id+'/journey.html?screen=results');await page.evaluate(h=>document.querySelector('#bookingSteps').outerHTML=h,native);const before=await page.evaluate(measure);await page.addStyleTag({content:patch});const after=await page.evaluate(measure);desktop.push({property:b.id,pass:JSON.stringify(before)===JSON.stringify(after)});}
 await browser.close();
 const evidence={scope:'Native DOM replay; later labels/action visibility are synthetic layout permutations, not native navigation or touch certification.',baseline,checks:rows,desktop};
 fs.writeFileSync(path.join(root,'verification.json'),JSON.stringify(evidence,null,2)+'\n');
 console.log(JSON.stringify({checks:rows.length,failures:rows.filter(x=>!x.pass),desktop,baseline:baseline.filter(x=>x.property==='kingfisher').map(x=>({width:x.width,height:x.height})),corrected:rows.filter(x=>x.property==='kingfisher'&&x.step===1&&x.action==='none').map(x=>({width:x.width,height:x.height}))}));
 if(rows.some(x=>!x.pass)||desktop.some(x=>!x.pass))process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
