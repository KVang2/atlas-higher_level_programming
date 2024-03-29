#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringWrite = process.argv[3];

if (!filePath || !stringWrite) {
  console.error('Error: file path or string not provided');
  process.exit(1);
}

fs.writeFile(filePath, stringWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
