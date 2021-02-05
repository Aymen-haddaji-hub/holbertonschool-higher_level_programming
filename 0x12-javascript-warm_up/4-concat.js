#!/usr/bin/node
let a = 'undefined';
let b = 'undefined';
if (process.argv[2]) {
  a = process.argv[2];
}
if (process.argv[3]) {
  b = process.argv[3];
}
console.log(`${a} is ${b}`);
