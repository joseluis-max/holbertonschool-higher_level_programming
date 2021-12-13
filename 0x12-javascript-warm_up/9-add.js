#!/usr/bin/node
const argv = require('process').argv;

const argvInt2 = parseInt(argv[2]);
const argvInt3 = parseInt(argv[3]);

add(argvInt2, argvInt3);
function add (a, b) {
  console.log(a + b);
}
