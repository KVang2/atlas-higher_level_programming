#!/usr/bin/node
exports.esrever = function (list) {
  // Get length of list
  const l = list.length;

  // Iterate over first half of the list
  // Swap elements to reverse list
  // Math.floor, used to convert floating point num to int
  for (let i = 0; i < Math.floor(l / 2); i++) {
    // swap elements using temp variable
    const temp = list[i];
    list[i] = list[l - 1 - i];
    list[l - 1 - i] = temp;
  }
  return list;
}
