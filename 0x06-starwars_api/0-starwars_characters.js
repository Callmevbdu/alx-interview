#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// - The first positional argument passed is the Movie ID -
// example: 3 = “Return of the Jedi”
// - Display one character name per line in the same order as the
// “characters” list in the /films/ endpoint
// - You must use the Star wars API
// - You must use the request module

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (err, res, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }

    if (res.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characters, index + 1); // Recursive call to print next character
    } else {
      console.error('Failed to fetch character data. Status code:', res.statusCode);
    }
  });
}
