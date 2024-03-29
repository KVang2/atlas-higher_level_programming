#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

if (!url) {
    console.error('Error: no URL');
    process.exit(1);
}

request.get(url)
    .then(response => {
        console.log(response.status);
    })
    .catch(error => {
        console.error('Error:, error occur');
        process.exit(1);
    });
