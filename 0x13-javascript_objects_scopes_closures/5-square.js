#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = this.height = size;
  }
}

module.exports = Square;