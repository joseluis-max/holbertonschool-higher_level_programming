#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/**
 * Represent a Square
 * @property { number } size
 * - size square
 * @extends Rectangle
 */
class Square extends Rectangle {
  /**
   * Create a new Square
   * @param { number } size - size square
   */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
