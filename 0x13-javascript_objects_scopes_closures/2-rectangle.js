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
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
