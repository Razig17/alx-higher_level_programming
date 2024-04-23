#!/usr/bin/node
let max = 0;
let max2 = '0';
let n = 0;
if (process.argv[3]) {
  max = parseInt(process.argv[2]);
  max2 = parseInt(process.argv[3]);
  if (max > max2) {
    n = max2;
    max2 = max;
    max = n;
  }
  for (let i = 2; i < process.argv.length; i++) {
    n = parseInt(process.argv[i]);
    if (n > max) {
      max2 = max;
      max = n;
    } else if (n > max2) {
      max2 = n;
    }
  }
}
console.log(max2);
