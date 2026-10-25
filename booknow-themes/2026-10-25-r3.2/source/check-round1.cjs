const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {chromium}=require('C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..'),brands=JSON.parse(fs.readFileSync(path.join(__dirname,'brands.json')));
const widths=[320,390,768,1024,1440,1920],states=process.env.R32_IDLE_ONLY?['idle']:['home','results','noavailability','rates','terms','photos','location','guest','idle'];
const base=process.env.R32_BASE||'http://127.0.0.1:9147';
const measure=()=>{
 const rect=e=>{if(!e)return null;const r=e.getBoundingClientRect();return{x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width,height:r.height}};
 const visible=e=>e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0;
 const text=[...document.querySelectorAll('#content .hotelNoRatesResult .leftColumn,#content .hotelNoRatesResult .info,#content .hotelDescription,#photoMount #formDetails p')].filter(visible).map(e=>({cls:e.className,client:e.clientWidth,scroll:e.scrollWidth,...rect(e)}));
 const controls=[...document.querySelectorAll('#searchBar input,#searchBar select,#searchBar button,.hotelInfo a,.standardButton,.smallButton,.viewAlternativeDatesLink,#bookingSteps>div>a,#formDetails input,#formDetails select,#formDetails textarea,#formButtons button,.navimages')].filter(visible).map(e=>({name:e.title||e.id||e.textContent.slice(0,30),type:e.type,...rect(e),labelHeight:e.type==='checkbox'?document.querySelector('label[for="'+e.id+'"]')?.getBoundingClientRect().height:null}));
 const steps=[...document.querySelectorAll('#bookingSteps .steps>div[class*=stepsName]')].filter(visible).map(e=>({cls:e.className,...rect(e),label:rect(e.querySelector('a')),badge:getComputedStyle(e.querySelector('a'),'::before').content,decorativeVisible:[...e.querySelectorAll('div')].some(visible)}));
 const thumbs=[...document.querySelectorAll('.hotelImage img,.hotelResultRoom .roomImage img')].filter(visible).map(e=>({natural:[e.naturalWidth,e.naturalHeight],...rect(e),parent:rect(e.closest('.hotelImage,.roomImage'))}));
 const photos=[...document.querySelectorAll('.imageCarousel #main .gallerylayer img')].filter(visible).map(e=>({natural:[e.naturalWidth,e.naturalHeight],...rect(e),fit:getComputedStyle(e).objectFit}));
 const logo=document.querySelector('#client_logo img');
 return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,text,controls,steps,thumbs,photos,logo:logo?{...rect(logo),natural:[logo.naturalWidth,logo.naturalHeight],fit:getComputedStyle(logo).objectFit}:null,dialog:rect(document.querySelector('.gwt-DialogBox')),hiddenActions:[...document.querySelectorAll('#bookingSteps [aria-hidden=true],#content .hotelRates [aria-hidden=true]')].filter(visible).length,hiddenPayment:!document.querySelector('#ccNumber')||!visible(document.querySelector('#ccNumber')),broken:[...document.images].filter(e=>visible(e)&&(!e.complete||!e.naturalWidth)).map(e=>e.getAttribute('src'))};
};
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true}),checks=[],transitions=[],shipping=[];
 const page=await browser.newPage();await page.route('**/*',r=>new URL(r.request().url()).origin===base?r.continue():r.abort());
 for(const b of brands){
  const manifest=JSON.parse(fs.readFileSync(path.join(root,'packages',b.id+'-manifest.json')));
  for(const n of ['mainStyle.css','theme.css','mobileTheme.css']){let rel='black-rhino2021/css/'+n;let raw=await(await page.request.get(base+'/package-css/'+b.id+'/'+rel)).body();let hash=crypto.createHash('sha256').update(raw).digest('hex');let pass=manifest.members.find(x=>x.path===rel).sha256===hash;if(!pass)throw Error('shipping mismatch '+b.id+n);shipping.push({property:b.id,file:n,hash,pass});}
  for(const state of states){for(const width of widths){
   await page.setViewportSize({width,height:width<500?900:1100});
   await page.goto(base+'/previews/'+b.id+'/'+(state==='home'?'home.html':'journey.html?screen='+state));await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(60);
   if(state==='home'){await page.waitForFunction(()=>{const e=document.querySelector('.imageCarousel .gallerylayer img')?.closest('.gallerylayer');return e&&Number(getComputedStyle(e).opacity)>.999});await page.evaluate(()=>document.querySelector('.navimages[title=Pause]')?.click());await page.waitForFunction(()=>[...document.querySelectorAll('.navimages')].every(e=>e.complete&&e.naturalWidth>0));}
   const m=await page.evaluate(measure);
   const badControls=m.controls.filter(x=>x.x< -1||x.right>width+1||(x.type==='checkbox'?x.labelHeight<43.99:x.height<43.99));
   const badText=m.text.filter(x=>x.scroll>x.client+1||(state==='idle'&&m.dialog&&x.cls===''&&x.width<m.dialog.width-70));
   const badThumbs=m.thumbs.filter(x=>x.width>Math.min(133,x.natural[0])+1||x.height>Math.min(99,x.natural[1])+1||x.right>x.parent.right+1||Math.abs(x.width/x.height-x.natural[0]/x.natural[1])>.02);
   const badPhotos=m.photos.filter(x=>x.width>x.natural[0]+1||Math.abs(x.width/x.height-670/300)>.02||x.fit!=='contain');
   const badSteps=m.steps.filter(x=>x.decorativeVisible||x.label.x<x.x-1||x.label.right>x.right+1||x.badge==='none');
   const dialogBad=m.dialog&&(m.dialog.x< -1||m.dialog.right>width+1||m.dialog.y< -1||m.dialog.bottom>(width<500?900:1100)+1);
   const pass=m.scrollWidth<=width+1&&!badControls.length&&!badText.length&&!badThumbs.length&&!badPhotos.length&&!badSteps.length&&!dialogBad&&!m.hiddenActions&&m.hiddenPayment&&!m.broken.length;
   checks.push({property:b.id,state,pass,...m,badControls,badText,badThumbs,badPhotos,badSteps,dialogBad});
   if([390,1440].includes(width)&&['home','noavailability','photos','idle'].includes(state))await page.screenshot({path:path.join(root,'previews',b.id,state+'-'+width+'.png'),fullPage:true,animations:'disabled'});
  }}
  if(process.env.R32_IDLE_ONLY)continue;
  await page.setViewportSize({width:390,height:900});await page.goto(base+'/previews/'+b.id+'/journey.html?screen=noavailability');await page.locator('.viewAlternativeDatesLink').click();let recovery=await page.locator('.hotelResultRoom').count()===1;await page.locator('#bookingSteps .backButton').click();recovery=recovery&&await page.locator('.hotelResult .hotelImage').count()===1;
  await page.locator('.fixtureToolbar [data-state=idle]').click();const ok=page.locator('#photoMount #formButtons button');await ok.focus();const focused=await ok.evaluate(e=>e===document.activeElement);await page.keyboard.press('Enter');const idleClose=focused&&await page.locator('#photoMount .gwt-DialogBox').count()===0;
  const stageRows=[];for(const width of widths){await page.setViewportSize({width,height:1100});for(let stage=1;stage<=4;stage++){await page.goto(base+'/previews/'+b.id+'/journey.html?screen=results&stage='+stage);const m=await page.evaluate(measure);stageRows.push({width,stage,pass:m.steps.length===(width<=960?1:4)&&m.steps.every(x=>!x.decorativeVisible&&x.label.x>=x.x-1&&x.label.right<=x.right+1)&&!m.hiddenActions});}}
  transitions.push({property:b.id,recovery,idleClose,stages:stageRows,pass:recovery&&idleClose&&stageRows.every(x=>x.pass)});
 }
 const transparentLogos=[];const logoDir=process.env.R32_LOGO_FIXTURE_DIR||path.resolve(root,'../2026-10-25-repair');
 if(!process.env.R32_IDLE_ONLY)for(const id of ['imbali','kwafubesi']){const file=path.join(logoDir,id+'-logo-original.png');if(!fs.existsSync(file))continue;const raw=fs.readFileSync(file);await page.route('**/cms-assets/'+id+'/logo-230x100.png',r=>r.fulfill({contentType:'image/png',body:raw}));for(const width of widths){await page.setViewportSize({width,height:1100});await page.goto(base+'/previews/'+id+'/journey.html?screen=noavailability');const m=await page.evaluate(()=>{const e=document.querySelector('#client_logo img'),r=e.getBoundingClientRect(),h=document.querySelector('#header').getBoundingClientRect();return{natural:[e.naturalWidth,e.naturalHeight],width:r.width,height:r.height,headerHeight:h.height,contained:r.top>=h.top-1&&r.bottom<=h.bottom+1,filter:getComputedStyle(e).filter}});const pass=m.natural[0]>0&&m.width<=m.natural[0]&&Math.abs(m.width/m.height-m.natural[0]/m.natural[1])<.01&&m.contained&&m.filter==='none';transparentLogos.push({property:id,viewport:width,sourceSha256:crypto.createHash('sha256').update(raw).digest('hex'),pass,...m});if(width===390)await page.screenshot({path:path.join(root,'previews',id,'transparent-logo-390.png'),fullPage:true});}}
 await browser.close();const result={round:1,method:'Existing native Imbali result + idle + native steps DOM. Other states use native selector vocabulary with authored data. Local transitions/keyboard are fixture-only; no native backend/touch/checkout certification. Optional original PNG logo overrides are preview-only and not shipped.',shipping,checks,transitions,transparentLogos};
 fs.writeFileSync(path.join(root,process.env.R32_IDLE_ONLY?'verification-idle.json':'verification.json'),JSON.stringify(result,null,2)+'\n');
 const failures=checks.filter(x=>!x.pass).map(x=>({property:x.property,state:x.state,width:x.width,scroll:x.scrollWidth,badControls:x.badControls,badText:x.badText,badThumbs:x.badThumbs,badPhotos:x.badPhotos,badSteps:x.badSteps,dialog:x.dialogBad?x.dialog:null,hidden:x.hiddenActions,broken:x.broken}));
 console.log(JSON.stringify({checks:checks.length,shipping:shipping.length,transitionChecks:transitions.length*26,logoChecks:transparentLogos.length,failures,transitionFailures:transitions.filter(x=>!x.pass),logoFailures:transparentLogos.filter(x=>!x.pass)}));if(failures.length||transitions.some(x=>!x.pass)||transparentLogos.some(x=>!x.pass))process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
