#!/usr/bin/node
const fs = require('fs');
const [, , file1, file2, destination] = process.argv;
const data1 = fs.readFileSync(file1, 'utf8');

const data2 = fs.readFileSync(file2, 'utf8');
fs.writeFileSync(destination, data1 + data2, 'utf-8');
