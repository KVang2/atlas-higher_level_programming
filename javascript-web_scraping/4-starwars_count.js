#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
const charId = 18

if (!api) {
    console.log('Error: no URL');
    process.exit(1);
}

request.get(api, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }

  const films = JSON.parse(body).results;
  let movieCount = 0;

films.forEach((movie) => {
    if (movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${charId}/`)) {
        movieCount++;
    }
  });

  console.log(movieCount);
});
