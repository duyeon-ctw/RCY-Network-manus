(()=>{
  const body=document.body,menu=document.querySelector('[data-menu]');
  menu?.addEventListener('click',()=>{const open=body.classList.toggle('menu-open');menu.setAttribute('aria-expanded',String(open))});
  document.querySelectorAll('.navlinks a').forEach(a=>a.addEventListener('click',()=>{body.classList.remove('menu-open');menu?.setAttribute('aria-expanded','false')}));
  document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
  document.querySelectorAll('[data-current-date]').forEach(el=>el.textContent=new Intl.DateTimeFormat('ko-KR',{year:'numeric',month:'long',day:'numeric',weekday:'long'}).format(new Date()));
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reveals=document.querySelectorAll('.reveal');
  if(!reduce&&'IntersectionObserver'in window){const io=new IntersectionObserver((entries,o)=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');o.unobserve(e.target)}}),{threshold:.12});reveals.forEach(x=>io.observe(x))}else reveals.forEach(x=>x.classList.add('visible'));
  const count=el=>{const target=Number(el.dataset.count||0),suffix=el.dataset.suffix||'',dec=Number(el.dataset.decimals||0),start=performance.now();const tick=t=>{const p=Math.min((t-start)/1200,1),v=target*(1-Math.pow(1-p,3));el.textContent=v.toFixed(dec)+suffix;if(p<1)requestAnimationFrame(tick)};requestAnimationFrame(tick)};
  const counters=document.querySelectorAll('[data-count]');
  if(!reduce&&'IntersectionObserver'in window){const io=new IntersectionObserver((entries,o)=>entries.forEach(e=>{if(e.isIntersecting){count(e.target);o.unobserve(e.target)}}),{threshold:.5});counters.forEach(x=>io.observe(x))}else counters.forEach(x=>x.textContent=(x.dataset.count||0)+(x.dataset.suffix||''));
  const toast=document.querySelector('[data-toast-box]');let timer;
  document.querySelectorAll('[data-toast]').forEach(btn=>btn.addEventListener('click',()=>{if(!toast)return;toast.querySelector('span').textContent=btn.dataset.toast||'요청이 반영되었습니다.';toast.classList.add('show');clearTimeout(timer);timer=setTimeout(()=>toast.classList.remove('show'),2500)}));
  document.querySelectorAll('.tabs button').forEach(btn=>btn.addEventListener('click',()=>{btn.parentElement.querySelectorAll('button').forEach(x=>x.classList.remove('active'));btn.classList.add('active')}));
})();
