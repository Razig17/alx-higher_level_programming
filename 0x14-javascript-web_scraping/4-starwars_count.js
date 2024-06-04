#!/usr/bin/node
const request = require('request');
const Url = process.argv[2];

request(Url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.endsWith('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
