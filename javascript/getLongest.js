//Given an array of numbers, find the number with the most digits.
function findLongest(array){
  let strArr = array.map((n) => n.toString().length);
  let longest = Math.max(...strArr);
  return array[strArr.indexOf(longest)];
}
//Reduce version - ${num} => str
function findLongest(array){
    return array.reduce((acc, cur) => (`${cur}`.length > `${acc}`.length) ? cur : acc);
}