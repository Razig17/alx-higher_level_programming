#!/usr/bin/node

const { dict } = require('./101-data');

const newUserDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!newUserDict[occurrences]) {
    newUserDict[occurrences] = [];
  }
  newUserDict[occurrences].push(userId);
}

console.log(newUserDict);
