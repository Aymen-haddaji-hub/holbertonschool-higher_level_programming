#!/usr/bin/node
function factorial (n) {
  if (n < 2 && n > 0) { return (1); } else if (n > 1) { return (n * factorial(n - 1)); } else { return (1); }
}
console.log(factorial(parseInt(process.argv[2])));
