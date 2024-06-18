#!/usr/bin/node
// 101-sorted.js

const dict = require('./101-data').dict;

// Function to invert the dictionary based on occurrences
function invertDictionary(dict) {
  const invertedDict = {};
  
  // Iterate over the original dictionary
  for (let userId in dict) {
    let occurrences = dict[userId];
    
    // If the occurrences key doesn't exist in invertedDict, create it as an empty array
    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }
    
    // Push the userId into the array corresponding to its occurrences
    invertedDict[occurrences].push(userId);
  }
  
  return invertedDict;
}

const invertedDict = invertDictionary(dict);

console.log(invertedDict);
