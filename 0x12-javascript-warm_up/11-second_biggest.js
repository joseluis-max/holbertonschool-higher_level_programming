#!/usr/bin/node
const argv = require('process').argv;

let a = 0;
let b = 0;

for (const number of argv) {
    if (!isNaN(parseInt(number))){
        if (number > a) {
            b = a;
            a = number;
        }
    }
}
console.log(b);
