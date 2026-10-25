const fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
const {chromium}=require('C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
const py='C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
const data=JSON.parse(execFileSync(py,['-c',"import pathlib,zipfile,json,sys; r=pathlib.Path(sys.argv[1]); print(json.dumps([{'property':p.name.split('-Legacy-')[0],'styles':{n:zipfile.ZipFile(p).read(n).decode('utf-8-sig') for n in ['black-rhino2021/css/mainStyle.css','black-rhino2021/css/theme.css','black-rhino2021/css/mobileTheme.css']}} for p in sorted((r/'packages').glob('*.zip'))]))",root],{encoding:'utf8',maxBuffer:8*1024*1024}));
(async()=>{let browser=await chromium.launch({channel:'chrome',headless:true}),page=await browser.newPage(),checks=[];
 await page.route('**/*',r=>r.abort());
 for(const b of data)for(const [file,css] of Object.entries(b.styles))for(const width of [390,1440]){
  await page.setViewportSize({width,height:900});
  await page.setContent('<div class="gwt-DialogBox"><div class="Caption"></div><div id="gallery"></div></div>');
  await page.addStyleTag({content:css});
  const empty=await page.locator('.Caption').evaluate(e=>getComputedStyle(e,'::before').content);
  await page.locator('.Caption').evaluate(e=>e.textContent='Native property caption');
  const supplied=await page.locator('.Caption').evaluate(e=>({text:e.textContent,fallback:getComputedStyle(e,'::before').content}));
  checks.push({property:b.property,file,width,empty,supplied,pass:empty==='"Photo gallery"'&&supplied.text==='Native property caption'&&['none','normal'].includes(supplied.fallback)});
 }
 await browser.close();fs.writeFileSync(path.join(root,'caption-verification.json'),JSON.stringify({scope:'Local browser rendering of exact shipping CSS. Empty fallback and supplied native caption; no application/backend/network.',checks},null,2)+'\n');
 console.log(JSON.stringify({checks:checks.length,failures:checks.filter(x=>!x.pass)}));if(checks.some(x=>!x.pass))process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)});
