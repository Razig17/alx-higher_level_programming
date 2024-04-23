#!/usr/bin/node
let i = 4;
let max = 0;
let max2 = 0;
let n = 0;
if (process.argv[3]) {
  max = parseInt(process.argv[2]);
  max2 = parseInt(process.argv[3]);
  if (max2 > max) {
    n = max2;
    max2 = max;
    max = max2;
    n = 0;
  }
  while (process.argv[i] !== undefined) {
    n = parseInt(process.argv[i]);
    if (n) {
      if (n > max) {
        max2 = max;
        max = n;
      } else if (n > max2) {
        max2 = n;
      }
    }
    i++;
  }
}
console.log(max2);
