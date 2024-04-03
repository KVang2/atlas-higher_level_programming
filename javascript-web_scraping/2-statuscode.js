#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Check if URL is provided
if (!url) {
  console.error('Error: no URL');
  process.exit(1);
}

// Make get request to the provided URL
request.get(url, (error, response) => {
  // Check for error during request
  if (error) {
    console.error('Error:', error.msg);
    process.exit(1);
  }
  // If no error, log status code of response
  console.log('code:', response.statusCode);
});
