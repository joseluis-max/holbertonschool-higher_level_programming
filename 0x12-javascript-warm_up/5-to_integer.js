#!/usr/bin/node
const argv = require('process').argv;
const argvInt = parseInt(argv[2]);
if (isNaN(argvInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argvInt);
}
