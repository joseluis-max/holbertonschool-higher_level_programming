#!/usr/bin/node
/** Reverse list */
exports.esrever = function (list) {
  const newList = [];
  for (item of list) {
    newList.unshift(item);
  }
  return newList;
};
