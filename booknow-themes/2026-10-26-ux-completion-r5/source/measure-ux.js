async () => {
 await document.fonts.ready;
 const tick=async()=>{await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);};
 const box=e=>e?.getBoundingClientRect().toJSON();
 const visible=e=>{if(!e)return false;const b=e.getBoundingClientRect(),s=getComputedStyle(e);return b.width>0&&b.height>0&&s.visibility!=='hidden'&&s.display!=='none';};
 const issues=()=>{
  const out=[];
  document.querySelectorAll('#content :is(p,h1,h2,h3,h4,h5,button,td,label,.gwt-HTML),#bookingSteps a,#sideBar label').forEach(e=>{
   if(!visible(e)||e.closest('.ratesDetails'))return;
   if(e.clientWidth>0&&e.scrollWidth>e.clientWidth+2)out.push({kind:'horizontal-content',tag:e.tagName,cls:e.className,text:e.textContent.slice(0,65),client:e.clientWidth,scroll:e.scrollWidth});
  });
  document.querySelectorAll('.hotelDescription,.roomDescription,.hotelFeatures').forEach(e=>{if(!visible(e))return;let parent=e.closest('.hotelResultRoom,.hotelInfoContent-open,.hotelResult');if(!parent)return;let a=box(e),b=box(parent);if(a.left<b.left-1||a.right>b.right+1)out.push({kind:'outside-parent',cls:e.className,rect:a,parent:b});});return out;
 };
 const rows=[],mobile=!!window.NATIVE_MOBILE_REPLAY;
 for(const state of mobile?['results','location','terms','photos']:['results','roominfo','location','terms','photos','rates']){
  render(state);await tick();
  const moving=document.getAnimations().filter(a=>a.playState==='running'&&a.effect.getTiming().iterations!==Infinity);
  await Promise.race([Promise.all(moving.map(a=>a.finished.catch(()=>{}))),new Promise(r=>setTimeout(r,1200))]);await tick();
  if(state==='photos'){document.querySelector('#gallery .navimages[title="Pause"]')?.click();await tick();}
  const step=document.querySelector('#bookingSteps .steps'),selected=step?.querySelector(':scope>div:has(>.selected)>a');
  const p=Array.from(document.querySelectorAll('.hotelInfoContent-open,.gwt-DialogBox:has(#gallery)')).filter(visible).pop(),close=p?.querySelector('.header,#formButtons button');
  const hit=()=>{if(!close)return false;let b=box(close),e=document.elementFromPoint(b.left+b.width/2,b.top+b.height/2);return e===close||close.contains(e);};
  let panel=null;
  if(p){const area=p.querySelector('.dialogContent>table>tbody>tr:first-child')||p;area.scrollTop=0;await tick();const top=hit();area.scrollTop=area.scrollHeight;await tick();panel={rect:box(p),close:box(close),closeHitTop:top,closeHitEnd:hit(),scrollRegion:box(area),innerScrollEnd:area.scrollTop,innerScrollMax:Math.max(0,area.scrollHeight-area.clientHeight),contentEndReachable:Math.abs(area.scrollHeight-area.clientHeight-area.scrollTop)<=2||area.scrollHeight<=area.clientHeight+1};area.scrollTop=0;}
  const icons=Array.from(document.querySelectorAll('.hotelFeatures img')).filter(visible).map(e=>({title:e.title||e.alt,rect:box(e),natural:[e.naturalWidth,e.naturalHeight]}));
  const iconCollisions=[];for(let i=0;i<icons.length;i++)for(let j=i+1;j<icons.length;j++){let a=icons[i].rect,b=icons[j].rect;if(a.left<b.right-1&&a.right>b.left+1&&a.top<b.bottom-1&&a.bottom>b.top+1)iconCollisions.push([i,j]);}
  const textIssues=issues();
  const row={state,mobile,width:innerWidth,height:innerHeight,documentWidth:document.documentElement.scrollWidth,tableReadability:mobile?'N/A native mobile hides desktop summary':'visible desktop table',progress:{display:step?getComputedStyle(step).display:null,current:selected?.textContent,rect:box(selected),currentBackground:selected?getComputedStyle(selected).backgroundColor:null,visibleStages:Array.from(step?.querySelectorAll(':scope>div[class*=stepsName]')||[]).filter(visible).map(e=>({text:e.textContent,current:!!e.querySelector('.selected')})),hiddenActionVisible:Array.from(document.querySelectorAll('#bookingSteps [aria-hidden="true"]')).some(visible)},actions:Array.from(document.querySelectorAll('.hotelRates button')).filter(visible).map(e=>({text:e.textContent,rect:box(e)})),icons,iconCollisions,textIssues,panel};
  row.pass=row.documentWidth<=innerWidth+1&&textIssues.length===0&&row.actions.every(a=>a.rect.width>=44&&a.rect.height>=44)&&iconCollisions.length===0&&!row.progress.hiddenActionVisible&&visible(selected)&&(!panel||(panel.rect.left>=-1&&panel.rect.right<=innerWidth+1&&panel.rect.top>=-1&&panel.rect.bottom<=innerHeight+1&&panel.closeHitTop&&panel.closeHitEnd));
  rows.push(row);
 }
 return rows;
}
