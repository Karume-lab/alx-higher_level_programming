#!/usr/bin/node

let big2 = process.argv[2];
if (big2 && (parseInt(big2))) {
  for (let index = 2; index < process.argv.length; index++) {
    if ((big2 < process.argv[index]) && (process.argv[index] !== process.argv[process.argv.length - 1])) {
      big2 = process.argv[index];
    }
  }
} else {
  big2 = 0;
}
console.log(big2);
