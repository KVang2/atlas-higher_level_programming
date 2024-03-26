#!/usr/bin/node

// Convert first argument to an integer
const num = parseInt(process.argv[2]);

// Check if argument can be converted to integer
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
    console.log('Missing number of occurrences', num);
}
