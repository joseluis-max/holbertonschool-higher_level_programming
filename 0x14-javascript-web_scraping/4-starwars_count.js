#!/usr/bin/node
const request = require('request');
const { stripVTControlCharacters } = require('util');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  body = JSON.parse(body);
  let count = 0;
  for (movie of body.results){
    for (c of movie.characters){
      if (/\/18\/$/.test(c)){
        count++;
      }
    }
  }
  console.log(count);
});
