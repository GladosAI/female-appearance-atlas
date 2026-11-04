// Standard npm dependencies. A custom browser is optional, never user-specific.
exports.playwright=require('playwright');
exports.sharp=require('sharp');
// Full Chromium's new headless mode follows the browser used by real visitors.
// The stripped headless shell differs in file:// storage behavior on Linux.
exports.browserOptions=process.env.ATLAS_BROWSER_EXECUTABLE?{executablePath:process.env.ATLAS_BROWSER_EXECUTABLE}:{channel:'chromium'};
