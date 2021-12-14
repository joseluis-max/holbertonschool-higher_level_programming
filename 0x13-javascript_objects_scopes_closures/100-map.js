#!/usr/bin/node
/** script that imports an array and computes a new array. */
let list = require('100-data.js');
newList = list.map((value, index)=> value * index);
console.log(list);
console.log(newList);
