#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Error: no URL');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error.msg);
    process.exit(1);
  }
  console.log('code:', response.statusCode);
});
