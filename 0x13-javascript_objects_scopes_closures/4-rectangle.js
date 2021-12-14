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

  /** Print rectangle with x */
  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  /** Exchanges the width and the height of the rectangle */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /** Multiples the width and the height of the rectangle by 2 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
