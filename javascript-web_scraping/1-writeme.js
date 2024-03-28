#!/usr/bin/node
const fs = require('fs')
const filePath = process.argv[2];

fs.writeFile(filePath, 'utf-8', data, (err) => {
  if (err) {
    console.error(err)
    return;
  }
  console.log(data);
})
