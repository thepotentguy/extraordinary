/* OFFLINE ONLY. Native property-specific markup; no booking application connected. */
const data=window.NATIVE_FIXTURE_DATA,params=new URLSearchParams(location.search);
let screen=params.get('screen')||'results';
const content=document.querySelector('#content'),mount=document.querySelector('#photoMount');
const clone=html=>{const t=document.createElement('template');t.innerHTML=html;return t.content;};
const detailBody=s=>s==='terms'?'<div class="paymentTerms"><section class="depositPolicy"><h3>Payment terms — layout replay</h3><p>Current selected-rate terms are not loaded in this offline replay. No deposit amount or payment deadline is asserted.</p></section><section class="cancelPolicy"><h3>Cancellation terms — layout replay</h3><p>No cancellation charge, refund or deadline is asserted. The live engine remains authoritative for the terms attached to a rate.</p></section></div>':'<div class="hotelLocation content"><div id="locationDetails"><h5>Location layout replay</h5><p>Live directions, coordinates and contact data are not loaded. This is an explicit layout placeholder, not a working map.</p></div><div class="locationMap"><div class="mapFixture"><strong>Map unavailable offline</strong><p>Native live map initialization and data remain unverified.</p></div></div><div class="clear_float"></div></div>';
const idle="<div class=\"gwt-DialogBox\" style=\"left: 1px; top: 328px; visibility: visible; position: absolute; overflow: visible;\"><div class=\"\"><table cellspacing=\"0\" cellpadding=\"0\" class=\"\" style=\"width: 370px; height: auto;\"><tbody><tr class=\"dialogTop\"><td class=\"dialogTopLeft\"><div class=\"dialogTopLeftInner\"></div></td><td class=\"dialogTopCenter\"><div class=\"dialogTopCenterInner\"><div class=\"Caption\">Message layout replay</div></div></td><td class=\"dialogTopRight\"><div class=\"dialogTopRightInner\"></div></td></tr><tr class=\"dialogMiddle\"><td class=\"dialogMiddleLeft\"><div class=\"dialogMiddleLeftInner\"></div></td><td class=\"dialogMiddleCenter\"><div class=\"dialogMiddleCenterInner dialogContent\"><div id=\"formDetails\"><div><p>Offline message layout replay. No live timeout, booking or guest state is connected.</p></div><div id=\"formButtons\"><button type=\"button\" class=\"gwt-Button\">OK</button></div></div></div></td><td class=\"dialogMiddleRight\"><div class=\"dialogMiddleRightInner\"></div></td></tr><tr class=\"dialogBottom\"><td class=\"dialogBottomLeft\"><div class=\"dialogBottomLeftInner\"></div></td><td class=\"dialogBottomCenter\"><div class=\"dialogBottomCenterInner\"></div></td><td class=\"dialogBottomRight\"><div class=\"dialogBottomRightInner\"></div></td></tr></tbody></table></div></div>\n";
function result(state){
 const f=clone(data.result),r=f.querySelector('.hotelResult');
 r.querySelectorAll('.hotelInfoContent').forEach(e=>e.classList.remove('hotelInfoContent-open'));
 r.querySelectorAll('button.viewRatesLink').forEach(b=>{b.disabled=false;b.textContent='View Rates · replay';b.dataset.state='rates';});
 if(state==='noavailability'||state==='idle'){
  const h=r.querySelector('.hotelHeading');h.insertAdjacentHTML('afterend','<div class="hotelNoRatesResult"><div class="leftColumn"><div id="message"><p class="info">No-availability layout replay. This is not a live inventory result. Use another date in the actual booking engine.</p></div></div><div class="rightColumn"><button class="viewAlternativeDatesLink" type="button" data-state="rates">View Alternative Dates · replay</button></div></div>');
  r.querySelector('.hotelRates').style.display='none';
 }
 if(state==='terms'||state==='location'||state==='roominfo'){
  const old=r.querySelector('.hotelInfoContent');
  if(state==='roominfo'){
   const p=clone(data.roomInfo).firstElementChild;p.classList.add('hotelInfoContent-open');p.style.removeProperty('display');old.replaceWith(p);
  }else{
   old.classList.add('hotelInfoContent-open');const rows=old.querySelectorAll('tr');rows[0].querySelector('a').textContent='Close';rows[0].querySelector('a').dataset.state='results';rows[1].querySelector('td').innerHTML='<div class="content">'+detailBody(state)+'</div>';
  }
 }
 content.replaceChildren(f);
 content.querySelectorAll('.hotelInfo a').forEach(a=>{a.dataset.state=a.classList.contains('pictureIcon')?'photos':a.classList.contains('locationIcon')?'location':a.classList.contains('paymentTermsIcon')?'terms':'roominfo';});
 content.querySelectorAll('.hotelInfoContent .header').forEach(a=>{a.dataset.state='results';if(!a.textContent.trim())a.textContent='Close';});
}
function render(next){
 screen=next;mount.replaceChildren();
 const step=document.querySelector('#bookingSteps');if(step)step.replaceWith(clone(['rates','loading','error'].includes(next)?data.stepsRates:data.steps).firstElementChild);
 if(next==='rates'||next==='loading'||next==='error'){
  content.replaceChildren(clone(data.rates));
  if(next==='loading'){const e=content.querySelector('.loading');if(e){e.style.display='block';e.removeAttribute('aria-hidden');e.insertAdjacentText('beforeend','Loading stress replay — no request is running.');}}
  if(next==='error'){const e=content.querySelector('#message')||content;e.insertAdjacentHTML('afterbegin','<p class="error">Error stress replay: no live request or booking was submitted. This message tests long error text and recovery layout.</p>');}
 }else if(next==='guest'){
  content.innerHTML='<div class="hotelHeading"><h1>Later guest / payment screens unavailable</h1><h2>No booking or hold was submitted to reach this step. No synthetic guest form is presented as native coverage.</h2></div>';
 }else result(next);
 if(next==='photos'||next==='longcaption'||next==='imagefailure'){
  result('results');mount.replaceChildren(clone(data.gallery));
  let frames=window.GALLERY_FRAMES.map(x=>[x[0],'',x[2],x[3]]);
  if(next==='longcaption')frames=frames.map(x=>[x[0],x[1],x[2],'LONG CAPTION STRESS REPLAY ONLY — '+x[3]+' — This deliberately extended caption checks wrapping, the full image index and clear separation from previous, pause, next and Close controls at the narrowest supported width.']);
  if(next==='imagefailure')frames[0][0]='../../cms-assets/intentional-missing-image-stress.jpg';
  createCarousel(frames,'gallery');
 }
 if(next==='idle')mount.innerHTML=idle;
 document.querySelector('.fixtureStatus').textContent='OFFLINE '+next.toUpperCase()+' · Native structure with redacted display values; no live inventory, booking, payment or accessibility enhancement';
 document.querySelectorAll('.fixtureToolbar [data-state]').forEach(a=>a.setAttribute('aria-current',a.dataset.state===next?'page':'false'));
 history.replaceState(null,'','?screen='+next);
}
document.addEventListener('click',e=>{
 if(e.target.closest('#photoMount #formButtons button')){render('results');return;}
 const state=e.target.closest('[data-state]');if(state){e.preventDefault();render(state.dataset.state);return;}
 if(e.target.closest('#header a,#searchBar a,#searchBar button,#content a,#content button'))e.preventDefault();
});
render(screen);
