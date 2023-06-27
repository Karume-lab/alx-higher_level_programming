#!/usr/bin/node

const factNum = parseInt(process.argv[2]);
function factorial (num) {
  if ((num === 0) || (num === 1) || (isNaN(factNum) === true)) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
factorial(factNum);
