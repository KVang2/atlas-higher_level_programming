#!/usr/bin/node
const url = process.argv[2];
const request = request ('require');

if (!url) {
    console.log('Error: no URL');
    process.exit(1);
}
