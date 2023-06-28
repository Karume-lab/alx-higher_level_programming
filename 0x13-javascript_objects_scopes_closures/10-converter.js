#!/usr/bin/node

exports.converter = function (base) {
  return function numConverter (num) {
    return num.toString(base);
  };
};
