#!/usr/bin/node

const sizeNum = parseInt(process.argv[2]);
if (sizeNum && (isNaN(sizeNum) === true)) {
  for (let i = 0; i < sizeNum; i++) {
    for (let j = 0; j < sizeNum; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
