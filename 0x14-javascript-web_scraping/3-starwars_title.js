#!/usr/bin/node
const request = require('request');
const adress = process.argv[2];
request(adress, function (error, adress, body) {
    console.log(error || JSON.parse(body).title);
});
