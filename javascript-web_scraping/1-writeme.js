#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];

// Check both file path and string to write are provided
if (!filePath || !stringWrite) {
  // print error if one or the other is missing
  console.error('Error: file path or string not provided');
  process.exit(1);
}

// Write string to file
fs.writeFile(filePath, stringWrite, 'utf-8', (err) => {
  if (err) {
    // If error occures during writing log error to console
    console.error(err);
  }
});
