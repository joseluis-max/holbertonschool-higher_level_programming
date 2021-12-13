#!/usr/bin/node
const argv = require('process').argv;
const argvInt = parseInt(argv[2]);
if (isNaN(argvInt)) {
  console.log('Missing size');
} else if (argvInt > 0) {
  const draw = [];
  for (let i = 0; i < argvInt; i++) {
    draw.push('X');
  }
  for (let j = 0; j < argvInt; j++) {
    console.log(draw.join(''));
  }
}
