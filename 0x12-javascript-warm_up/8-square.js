#!/usr/bin/node
const n = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let row = '';
if (n) {
  while (i < n) {
    j = n;
    row = '';
    while (j > 0) {
      row += 'X';
      j--;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
