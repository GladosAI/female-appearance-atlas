// Standard npm dependencies. A custom browser is optional, never user-specific.
exports.playwright=require('playwright');
exports.sharp=require('sharp');
// Full Chromium's new headless mode follows the browser used by real visitors.
// The stripped headless shell differs in file:// storage behavior on Linux.
exports.browserOptions=process.env.ATLAS_BROWSER_EXECUTABLE?{executablePath:process.env.ATLAS_BROWSER_EXECUTABLE}:{channel:'chromium'};
// Offline persistence checks use a temporary regular profile, matching a visitor
// opening the downloaded site. HTTP checks keep an isolated incognito context.
exports.launchBrowser=async()=>{
 if(process.env.ATLAS_TEST_URL&&!process.env.ATLAS_TEST_URL.startsWith('file:'))return exports.playwright.chromium.launch({...exports.browserOptions,headless:true});
 const context=await exports.playwright.chromium.launchPersistentContext('',{...exports.browserOptions,headless:true,acceptDownloads:true});
 return {newPage:async(options={})=>{const page=await context.newPage();if(options.viewport)await page.setViewportSize(options.viewport);return page},close:()=>context.close()};
};
