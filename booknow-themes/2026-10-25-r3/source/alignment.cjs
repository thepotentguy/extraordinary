const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/poten/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true}),p=await browser.newPage();let rows=[];
for(const width of [1440,1024,768,390,320]){
 await p.setViewportSize({width,height:1000});await p.goto((process.env.R3_BASE||'http://127.0.0.1:9144')+'/previews/imbali/home.html');await p.evaluate(()=>document.fonts.ready);
 const d=await p.evaluate(()=>{const box=s=>{const e=document.querySelector(s);return e?e.getBoundingClientRect().toJSON():null};return{width:innerWidth,wrapper:box('#contentWrapper'),search:box('#searchBar'),feed:box('#newsFeeds'),table:box('#newsFeeds .newsFeedFlexTable'),panel:box('#newsFeeds .newsFeedItemPanel'),gallery:box('.imageCarousel'),main:box('#main'),date:box('#stayCriteria'),occupancy:box('#unitBreakdown'),promo:box('#promoCriteria'),cta:box('.submitBtnContainer')}});
 const eq=(a,b)=>Math.abs(a-b)<=1;
 d.aligned=eq(d.search.x,d.panel.x)&&eq(d.search.right,d.panel.right)&&eq(d.search.x,d.main.x)&&eq(d.search.right,d.main.right);
 rows.push(d);
}
await browser.close();fs.writeFileSync(path.join(root,'private-evidence',process.env.R3_BASE?'alignment-after.json':'alignment-before.json'),JSON.stringify(rows,null,2));console.log(JSON.stringify(rows.map(r=>({width:r.width,pass:r.aligned,search:[r.search.x,r.search.right],panel:[r.panel.x,r.panel.right],main:[r.main.x,r.main.right],bookingTops:[r.date.y,r.occupancy.y,r.promo.y,r.cta.y]})),null,2));if(rows.some(r=>!r.aligned))process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1)})
