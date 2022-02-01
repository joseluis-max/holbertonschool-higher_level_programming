#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
    if (err) throw err;
    body = JSON.parse(body);
    console.log(body.title);
});
