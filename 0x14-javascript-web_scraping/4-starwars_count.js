#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  body = JSON.parse(body);
  let count = 0;
  for (const movie of body.results) {
    for (const c of movie.characters) {
      if (/\/18\/$/.test(c)) {
        count++;
      }
    }
  }
  console.log(count);
});
