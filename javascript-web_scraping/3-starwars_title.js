#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];

if (!arg) {
    console.error('Error: no URL');
    process.exit(1);
}

const api =  'https://swapi-api.hbtn.io/api/films/${arg}';

request.get(api, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        process.exit(1);
    }
    if (response.statusCode !== 200) {
        console.error('Error:', response.statusCode, response.statusMessage);
        process.exit(1);
    }
const movie = JSON.parse(body);
const title = movie.title;
console.log('Title:', title);
});
