#!/usr/bin/node
const addMeMaybe = function (x, theFunction) {
  x++;
  theFunction(x);
};
exports.addMeMaybe = addMeMaybe;
