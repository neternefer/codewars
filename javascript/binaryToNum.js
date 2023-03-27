//Given an array of 1s and 0s, return decimal value
const binaryArrayToNumber = arr => {
  return arr.reverse()
  .map(function(e, i){return e ? 2**i : 0})
  .reduce((prev, cur) => prev + cur)
};

binaryArrayToNumber([0, 1, 0, 1] )