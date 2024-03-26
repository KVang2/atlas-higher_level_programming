#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));
function secondint(int) {
  if (int.length < 2) {
    return 0;
  }
  const sortedint = int.sort((a, b) => b - a);
  return sortedint[1];
}
console.log(secondint(args));
