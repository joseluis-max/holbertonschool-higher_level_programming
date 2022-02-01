#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  body = JSON.parse(body);
  let result = {};

  for (task of body){
    if (result[task.userId] != undefined && task.completed == true){
      result[task.userId] += 1;
    }
    else if (result[task.userId] == undefined && task.completed == true){
      result[task.userId] = 1;
    }
  }
  console.log(result);
});
