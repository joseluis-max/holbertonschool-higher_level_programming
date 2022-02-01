#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;
  body = JSON.parse(body);
  const result = { };

  for (const task of body) {
    if (result[task.userId] !== undefined && task.completed === true) {
      result[task.userId] += 1;
    } else if (result[task.userId] === undefined && task.completed === true) {
      result[task.userId] = 1;
    }
  }
  console.log(result);
});
