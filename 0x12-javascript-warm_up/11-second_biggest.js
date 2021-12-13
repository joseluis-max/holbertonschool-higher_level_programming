#!/usr/bin/node
const argv = require('process').argv;

if (argv.length === 3 || argv.length === 2) {
  console.log(0);
} else {
  argv.sort((a, b) => {
    return a - b;
  });
  console.log(argv[argv.length - 2]);
}
