#!/usr/bin/node

const list = require('./100-data.js').list;
const newList = list.map((double, index) => double * index);

console.log(list);
console.log(newList);
