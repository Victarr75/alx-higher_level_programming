#!/usr/bin/node
// 6-square.js

// Import the Square class from 5-square.js
const SquareBase = require('./5-square');

// Define the Square class that extends SquareBase
class Square extends SquareBase {
  charPrint (c) {
    // Use the character 'X' if 'c' is undefined
    const char = c === undefined ? 'X' : c;

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

// Export the Square class
module.exports = Square;
