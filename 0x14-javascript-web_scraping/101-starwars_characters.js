#!/usr/bin/node
const request = require('request');
const util = require('util');
const get = util.promisify(request.get);
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

get(url).then(async (response) => {
  const movie = JSON.parse(response.body);
  for (const characterUrl of movie.characters) {
    const characterResponse = await get(characterUrl);
    const character = JSON.parse(characterResponse.body);
    console.log(character.name);
  }
}).catch((error) => {
  console.error(error);
});
