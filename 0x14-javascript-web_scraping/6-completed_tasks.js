#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (const completed of todos) {
      if (todos.completed === true) {
        if (todos.userId in completed) { completed[completed.userId]++; } else { completed[completed.userId] = 1; }
      }
    }
    console.log(completed);
  }
});
