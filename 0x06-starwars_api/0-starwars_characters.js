#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// 	- The first positional argument passed is the Movie ID -
// 	example: 3 = “Return of the Jedi”
// 	- Display one character name per line in the same order as the
// 	“characters” list in the /films/ endpoint
// 	- You must use the Star wars API
// 	- You must use the request module

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character data:', charError);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
