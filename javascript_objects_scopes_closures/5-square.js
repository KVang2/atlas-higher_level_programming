#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      this.width = w;
      this.height = h;
    }
}
module.exports = Rectangle;

class Square extends Rectangle {
    constructor (size) {
        super(size, size);
        this.size = size;
    }
}

module.exports = Square;