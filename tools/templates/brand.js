const brandThemeSettings=__BRAND_THEME_SETTINGS__;
const brandSystemScheme=window.matchMedia('(prefers-color-scheme: dark)');
function updateBrandAppearance(theme){
  const resolved=theme==='system'?(brandSystemScheme.matches?'dark':'light'):theme;
  const settings=brandThemeSettings[resolved]||brandThemeSettings.light;
  document.getElementById('site-favicon').setAttribute('href',settings.icon);
  document.getElementById('brand-theme-color').setAttribute('content',settings.background);
}
brandSystemScheme.addEventListener('change',()=>{
  if(document.documentElement.dataset.theme==='system')updateBrandAppearance('system');
});
