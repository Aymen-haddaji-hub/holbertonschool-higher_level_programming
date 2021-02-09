#!/usr/bin/node
const request = require('request');
const adress = 'http://swapi.co/api/films/' + process.argv[2];
request(adress, function (error, _adress, body) {
  console.log(error || JSON.parse(body).title);
});
