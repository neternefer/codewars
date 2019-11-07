/*Given a string of space separated numbers, 
return the highest and lowest number.
*/
function highAndLow(numbers){
  let arr = numbers.split(" ").map(e => Number(e));
  return Math.max(...arr).toString() + " " + Math.min(...arr).toString()
}
