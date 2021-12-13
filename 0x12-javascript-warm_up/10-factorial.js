#!/usr/bin/node
const argv = require('process').argv;

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 2) {
    return 2;
  }
  return x * factorial(x - 1);
}
const argvInt = parseInt(argv[2]);

console.log(factorial(argvInt));
