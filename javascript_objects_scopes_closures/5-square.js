#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      this.width = w;
      this.height = h;
    }
}

class Square extends Rectangle {
    constructor (size) {
        super(Rectangle);
        this.size = size;
    }
}

module.exports = Square;