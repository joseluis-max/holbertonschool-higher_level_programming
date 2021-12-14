#!/usr/bin/node
/** Return the occurences number */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
