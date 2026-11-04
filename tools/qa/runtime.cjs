// Standard npm dependencies. A custom browser is optional, never user-specific.
exports.playwright=require('playwright');
exports.sharp=require('sharp');
exports.browserOptions=process.env.ATLAS_BROWSER_EXECUTABLE?{executablePath:process.env.ATLAS_BROWSER_EXECUTABLE}:{};
