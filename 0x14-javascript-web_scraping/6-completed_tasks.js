#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completed = {}
    for (const x of todos) {
      if (x.completed === true) {
        if (x.userId in completed) { completed[x.userId]++; } else { completed[x.userId] = 1; }
      }
    }
    console.log(completed);
  }
});
