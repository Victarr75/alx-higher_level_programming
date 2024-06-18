#!/usr/bin/node
const fs = require('fs');

// Get command-line arguments
const args = process.argv.slice(2);
if (args.length !== 3) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

// Extract file paths
const fileA = args[0];
const fileB = args[1];
const fileC = args[2];

// Function to read file contents
function readFileContents(filePath) {
  try {
    return fs.readFileSync(filePath, 'utf8');
  } catch (err) {
    console.error(`Error reading file ${filePath}:`, err.message);
    process.exit(1);
  }
}

// Read contents of fileA and fileB
const contentA = readFileContents(fileA);
const contentB = readFileContents(fileB);

// Concatenate contents
const concatenatedContent = `${contentA}\n${contentB}`;

// Write concatenated content to fileC
try {
  fs.writeFileSync(fileC, concatenatedContent);
  console.log(`Concatenated contents of ${fileA} and ${fileB} saved to ${fileC}`);
} catch (err) {
  console.error(`Error writing to file ${fileC}:`, err.message);
  process.exit(1);
}
