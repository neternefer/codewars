//Return the sum of elements of combined arrays
function arrayPlusArray(arr1, arr2) {
    return arr1.concat(arr2).reduce((prev, cur) => prev + cur)
  }