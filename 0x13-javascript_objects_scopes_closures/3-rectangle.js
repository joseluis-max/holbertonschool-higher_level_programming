#!/usr/bin/node
/**
 * Represent a Rectangle
 * @property { number } width
 * - width rectangle
 * @property { number } height
 * - height rectangle
 */
class Rectangle {
  /**
   * Create a new Rectangle
   * @param { number } w - width Rectagle
   * @param { number } h - height Rectangle
   * @method print - print rectangle with "X"
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /** Print rectangle with x */
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
