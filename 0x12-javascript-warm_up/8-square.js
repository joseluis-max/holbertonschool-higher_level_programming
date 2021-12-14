#!/usr/bin/node
const argv = require('process').argv;
const argvInt = parseInt(argv[2]);
if (isNaN(argvInt)) {
  console.log('Missing size');
} else if (argvInt > 0) {
  for (let j = 0; j < argvInt; j++) {
    console.log("X".repeat(argvInt));
  }
}
