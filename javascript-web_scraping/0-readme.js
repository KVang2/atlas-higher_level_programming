#!/usr/bin/node

// Import 'fs' module
const fs = require('fs');
// Get file path provided as first argument
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
