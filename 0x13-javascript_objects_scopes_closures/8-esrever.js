#!/usr/bin/node
/** Reverse list */
exports.esrever = function (list) {
  const newList = [];
  let item;
  for (item of list) {
    newList.unshift(item);
  }
  return newList;
};
