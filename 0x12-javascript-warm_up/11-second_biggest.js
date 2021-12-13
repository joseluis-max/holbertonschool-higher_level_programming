#!/usr/bin/node
const argv = require('process').argv;

let a = argv[2];
let b = 0;
if (argv.length === 3 || argv.length === 2){
    console.log(0);
} else {
  for (const number of argv) {
    if (isNaN(parseInt(number > a))) {
      b = a;
      a = number;
    }
  }
  console.log(b);
}