#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let c = 0;
    for (const movie of results) {
      if (movie.characters.find(value => value.endsWith('18/'))) {
        c++;
      }
    }
    console.log(c);
  }
});
