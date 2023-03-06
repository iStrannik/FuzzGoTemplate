'use strict';

const puppeteer = require('puppeteer');    
(async() => {    
const browser = await puppeteer.launch();
const page = await browser.newPage();   
let pwned = 'safe_code';
var fs = require("fs");
var pathToFile = fs.readFileSync(0).toString(); // STDIN_FILENO = 0
page.on('dialog', async dialog => {
    pwned = 'pwned_succesfull';
    await dialog.dismiss();
	});
await page.goto('file://' + pathToFile);
console.log(pwned);    
await browser.close();    
})();