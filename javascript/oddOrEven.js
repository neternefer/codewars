function oddOrEven(array) {
    /**
     * Given a list of integers, determine whether the sum of its elements is odd or even.
       Give your answer as a string matching "odd" or "even".
       if arr == [] -> 'even'
     */
    return array.length == 0 || array.reduce((prev, cur) => prev + cur) % 2 == 0 ? 'even' : 'odd';
}

console.log(oddOrEven([]))