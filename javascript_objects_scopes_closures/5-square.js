#!/usr/bin/node
cl Rectangle = requestAnimationFrame('./4-rectangle.js');

class Square extends Rectangle {
    constructor (size) {
        super(size, size);
        this.size = size;
    }
}
module.exports = Square;
