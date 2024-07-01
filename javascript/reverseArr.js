function reverseArr(arr) {
    //Use reduceRight to reverse an array without mutating it.
    return arr.reduceRight((prev, cur) =>  prev.concat(cur), []);
}

console.log(reverseArr([1, 2, 3, 4, 5]))