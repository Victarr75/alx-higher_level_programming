# JavaScript Programming

## Why JavaScript Programming is Amazing

JavaScript is versatile and essential for web development, enabling dynamic content and interactive features.

## How to Run a JavaScript Script

- **In a Browser**: Include your script in an HTML file.
- **In Node.js**: Save your script in a file (e.g., `script.js`) and run it with `node script.js`.

## Creating Variables and Constants

```javascript
var variable1 = "var variable";
let variable2 = "let variable";
const constantVariable = "const variable";
```

## Differences Between `var`, `const`, and `let`

- `var`: Function-scoped or globally-scoped.
- `let`: Block-scoped.
- `const`: Block-scoped, cannot be updated or re-declared.

## Data Types in JavaScript

- String
- Number
- Boolean
- Null
- Undefined
- Object
- Symbol (ES6)
- BigInt (ES2020)

## Using `if`, `if...else` Statements

```javascript
let number = 10;
if (number > 5) {
    console.log("Number is greater than 5");
} else {
    console.log("Number is 5 or less");
}
```

## Using Comments

```javascript
// Single-line comment
/* Multi-line
   comment */
```

## Affecting Values to Variables

```javascript
let a = 5;
let b = 10;
a = b;  // a now equals 10
```

## Using `while` and `for` Loops

```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

## Using `break` and `continue` Statements

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i);
}

for (let i = 0; i < 10; i++) {
    if (i === 5) continue;
    console.log(i);
}
```

## Functions

```javascript
function greet(name) {
    return "Hello, " + name;
}

console.log(greet("World"));  // Output: Hello, World
```

A function that does not use any return statement returns `undefined`.

## Scope of Variables

- **Global Scope**: Declared outside any function or block.
- **Function Scope**: Declared within a function using `var`.
- **Block Scope**: Declared within a block using `let` or `const`.

## Arithmetic Operators

```javascript
let a = 10;
let b = 5;
console.log(a + b);  // Output: 15
console.log(a - b);  // Output: 5
console.log(a * b);  // Output: 50
console.log(a / b);  // Output: 2
console.log(a % b);  // Output: 0
```

## Manipulating Objects

```javascript
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30
};

console.log(person.firstName);  // Output: John
person.gender = "male";
delete person.age;
```

## Importing a File

- **Node.js**: `const module = require('./module.js');`
- **ES6+**: `import module from './module.js';`

