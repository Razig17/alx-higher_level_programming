#!/usr/bin/node

function factorial (n) {
  if (n > 0) {
    return n * factorial(n - 1);
  }
  return 1;
}
let result = 1;
const n = parseInt(process.argv[2]);
if (n) {
  result = factorial(n);
}
console.log(result);
