#!/usr/bin/node
const n = parseInt(process.argv[2]);
let i = 0;
if (n) {
  while (i < n) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
