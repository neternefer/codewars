//Check if the given array of numbers is in ascending order
function inAscOrder(arr) {
  let newArr =  arr.slice(1)
  return newArr.map((elem, index) => elem > arr[index])
        .every(elem => elem == true);
}