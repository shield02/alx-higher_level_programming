#!/usr/bin/node

const fs = require('fs');

const first = fs.readFileSync(process.argv[2], 'utf8', function (err) { if (err) console.log('error', err); });
const second = fs.readFileSync(process.argv[3], 'utf8', function (err) { if (err) console.log('error', err); });

const third = first.concat(second);

fs.writeFile(process.argv[4], third, 'utf8', function (err) { if (err) console.log('error', err); });
