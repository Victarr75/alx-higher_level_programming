#!/usr/bin/node
// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define the Square class that extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Calls the parent class constructor with size for both width and height
  }
}

// Export the Square class
module.exports = Square;
