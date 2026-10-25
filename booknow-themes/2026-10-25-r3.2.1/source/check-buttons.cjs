const fs=require('fs'),path=require('path'),crypto=require('crypto');
const{chromium}=require('C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..'),brands=JSON.parse(fs.readFileSync(path.join(__dirname,'brands.json'))),widths=[320,390,768,1024,1440,1920];
const metrics=()=>{
 const box=e=>{if(!e)return null;const r=e.getBoundingClientRect();return{x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width,height:r.height}};
 const visible=e=>e&&e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0;
 const overlap=(a,b)=>a&&b&&Math.min(a.right,b.right)-Math.max(a.x,b.x)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>1;
 const selectors=['.hotelNoRatesResult>.rightColumn>button.viewAlternativeDatesLink','.hotelResult .hotelRates>button.standardButton','button.viewRatesLink','.hotelResultRoom .roomRates>button.smallButton'];
 const controls=[...document.querySelectorAll(selectors.join(','))].filter(visible).map(e=>{
  let parent=e.parentElement,r=box(e),p=box(parent),s=getComputedStyle(e);
  const text=e.matches('.viewAlternativeDatesLink')?e.closest('.hotelNoRatesResult').querySelector('.leftColumn'):e.matches('.smallButton')?parent.querySelector('.ratesText'):null;
  const t=visible(text)?box(text):null,margins=[s.marginTop,s.marginRight,s.marginBottom,s.marginLeft];
  const contained=r.x>=p.x-1&&r.right<=p.right+1&&r.y>=p.y-1&&r.bottom<=p.bottom+1;
  return{class:e.className,button:r,parent:{class:parent.className,...p},message:t,margins,contained,overlap:overlap(r,t),zeroMargins:margins.every(x=>parseFloat(x)===0)};
 });
 return{width:innerWidth,pageWidth:document.documentElement.scrollWidth,controls,pass:controls.length>0&&controls.every(x=>x.contained&&!x.overlap&&x.zeroMargins)};
};
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true}),p=await browser.newPage(),before=[],checks=[],shipping=[];
 // R3.2 controls reproduce the actual native failure before the new assertion can pass.
 await p.route('**/package-css/**/*.css',async r=>{const resp=await r.fetch(),text=(await resp.text()).split('\n/* R3.2.1 round two:')[0];await r.fulfill({response:resp,body:text})});
 for(const b of brands){await p.setViewportSize({width:1920,height:1100});await p.goto('http://127.0.0.1:9148/previews/'+b.id+'/journey.html?screen=noavailability');await p.evaluate(()=>document.fonts.ready);before.push({property:b.id,state:'noavailability',...await p.evaluate(metrics)});}
 if(!before.some(x=>x.controls.some(c=>!c.contained&&c.overlap&&parseFloat(c.margins[3])<0)))throw Error('Baseline did not reproduce negative-margin overlap');
 await p.unroute('**/package-css/**/*.css');
 await p.route('**/*',r=>new URL(r.request().url()).origin==='http://127.0.0.1:9148'?r.continue():r.abort());
 for(const b of brands){let manifest=JSON.parse(fs.readFileSync(path.join(root,'packages',b.id+'-manifest.json')));
  for(const n of['mainStyle.css','theme.css','mobileTheme.css']){const rel='black-rhino2021/css/'+n,raw=await(await p.request.get('http://127.0.0.1:9148/package-css/'+b.id+'/'+rel)).body(),hash=crypto.createHash('sha256').update(raw).digest('hex');if(hash!==manifest.members.find(x=>x.path===rel).sha256)throw Error('Shipping hash mismatch');shipping.push({property:b.id,file:n,hash});}
  for(const state of['noavailability','results','rates'])for(const width of widths){
   await p.setViewportSize({width,height:1100});await p.goto('http://127.0.0.1:9148/previews/'+b.id+'/journey.html?screen='+state);await p.evaluate(()=>document.fonts.ready);
   if(state==='rates')await p.evaluate(()=>{const row=document.createElement('div');row.className='viewRateGrid';const b=document.createElement('button');b.type='button';b.className='viewRatesLink';b.textContent='View rates for more dates';row.append(b);document.querySelector('.roomsAndRates').prepend(row)});
   const m=await p.evaluate(metrics);checks.push({property:b.id,state,...m});
   if(state==='noavailability'&&[390,1920].includes(width))await p.screenshot({path:path.join(root,'previews',b.id,'noavailability-'+width+'.png'),fullPage:true,animations:'disabled'});
  }
 }
 await browser.close();fs.writeFileSync(path.join(root,'verification.json'),JSON.stringify({version:'R3.2.1',round:2,scope:'Native Imbali result nesting reused across five brand CSS variants; authored results/rates state data. Extra native-class viewRatesLink row is a local CSS margin fixture. No backend/search/native input certification.',before,checks,shipping},null,2)+'\n');
 const failures=checks.filter(x=>!x.pass);console.log(JSON.stringify({baselineCases:before.length,baselineFailures:before.filter(x=>!x.pass).length,targetedCases:checks.length,shippingHashes:shipping.length,failures}));if(failures.length)process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
