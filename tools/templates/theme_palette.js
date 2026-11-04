const themeSelect=document.getElementById('theme-select');
function setAppearance(theme,persistChoice=false){
  if(![...themeSelect.options].some(option=>option.value===theme))theme='system';
  document.documentElement.dataset.theme=theme;
  updateBrandAppearance(theme);
  themeSelect.value=theme;
  if(persistChoice){try{localStorage.setItem('female-beauty-theme-v2',theme)}catch{}}
}
setAppearance(document.documentElement.dataset.theme||'system');
themeSelect.addEventListener('change',()=>setAppearance(themeSelect.value,true));
