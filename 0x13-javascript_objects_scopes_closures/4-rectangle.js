#!/usr/bin/node
// 4-rectangle.js

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if dimensions are invalid
      return {};
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate() {
    // Swap width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // Double width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
