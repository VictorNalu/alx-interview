#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from the command line argument
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const movieData = JSON.parse(body); // Parse the JSON response
  const characters = movieData.characters; // Get the list of character URLs

  // Iterate over the list of characters
  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name); // Print the character name
    });
  });
});
