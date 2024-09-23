#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

// Ensure the URL is constructed correctly using template literals
request(`${url}${process.argv[2]}`, function (err, res, body) {
  if (err) throw err;

  // Parse the response body
  const characters = JSON.parse(body).characters;

  // Call exactOrder function to fetch character details
  exactOrder(characters, 0);
});

// Define the exactOrder function to fetch character names in order
const exactOrder = (characters, index) => {
  if (index === characters.length) return; // Base case for recursion

  request(characters[index], function (err, res, body) {
    if (err) throw err;

    // Print the character name
    console.log(JSON.parse(body).name);

    // Recursive call to fetch the next character
    exactOrder(characters, index + 1);
  });
};
