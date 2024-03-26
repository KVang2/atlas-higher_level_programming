#!/usr/bin/node

// Convert first argument to an integer
const num = parseInt(process.argv[2]);

// Check if argument can be converted to integer
if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
