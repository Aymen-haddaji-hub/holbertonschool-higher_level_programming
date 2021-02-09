#!/usr/bin/node
const request = require('request');
const adress = process.argv[2];
request(adress, function (error, adress) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + adress.statusCode);
  }
});
