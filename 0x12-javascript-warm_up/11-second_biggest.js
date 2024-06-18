#!/usr/bin/node

function secondBiggest(args) {
    if (args.length <= 1) {
        return 0;
    }

    let first = parseInt(args[0]);
    let second = parseInt(args[1]);

    if (first < second) {
        [first, second] = [second, first];
    }

    for (let i = 2; i < args.length; i++) {
        let num = parseInt(args[i]);
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num !== first) {
            second = num;
        }
    }

    return second;
}

const args = process.argv.slice(2);
console.log(secondBiggest(args));
