#!/usr/bin/node
function exports.nbOccurences = function (list, searchElement) {
    const occur = {};

    for (const ele of list) {
        occur[ele] = (occur[ele] || 0) + 1;
    }

    return occur[searchElement] || 0;
};