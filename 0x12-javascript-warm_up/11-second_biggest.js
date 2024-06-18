#!/usr/bin/node

function secondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  let first = parseInt(args[0], 10);
  let second = parseInt(args[1], 10);

  if (first < second) {
    [first, second] = [second, first];
  }

  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i], 10);
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num !== first) {
      second = num;
    }
  }

  return second;
}
