#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

if (!file) {
    console.error('Error: object error')
    process.exit(1);
}

try {
    const fileContent = fs.readFileSync(file, 'utf-8');
    console.log('FIle contents:', fileContent);
} catch (error) {
    console.error('Error reading file:', error.message);
    process.exit(1);
}