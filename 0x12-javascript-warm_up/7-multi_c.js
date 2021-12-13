#!/usr/bin/node
const argv = require('process').argv;
const argvInt = parseInt(argv[2]);
if (isNaN(argvInt)) {
  console.log('Missing number of occurrences');
} else if (argvInt > 0) {
  for (let i = 0; i < argvInt; i++) {
    console.log('C is fun');
  }
}
