#!/usr/bin/node
/**
 * script that imports a dictionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 */
const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  const element = dict[key];
  if (newDict[element]) {
    newDict[element].push(key);
  } else {
    newDict[element] = [key];
  }
}
console.log(newDict);
