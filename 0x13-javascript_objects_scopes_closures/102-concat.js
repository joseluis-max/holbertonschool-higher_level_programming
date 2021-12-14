#!/usr/bin/node
/** Write a script that concats 2 files. */
const argv = require('process').argv;
const fs = require('fs');
const firstData = fs.readFileSync(argv[2], 'utf8');
const secondData = fs.readFileSync(argv[3], 'utf8');
fs.writeFileSync(argv[4], firstData + '\n' + secondData + '\n');
