#!/usr/bin/node

function add(a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    return parseInt(a) + parseInt(b);
  }
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const result = add(arg1, arg2);
if (result !== undefined) {
    console.log(result);
} else {
    console.log(arg1 + arg2);
}
