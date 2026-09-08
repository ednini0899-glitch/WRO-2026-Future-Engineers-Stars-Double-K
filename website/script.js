const menu=document.querySelector('.menu-btn');
const links=document.querySelector('.nav-links');
menu?.addEventListener('click',()=>links.classList.toggle('open'));
links?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));
const items=document.querySelectorAll('.section,.team-card,.features article,.process-grid article,.gallery figure,.log article');
const observer=new IntersectionObserver(entries=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target);}
  });
},{threshold:.08});
items.forEach(el=>{el.classList.add('reveal');observer.observe(el);});
