function sum (numbers) {
   /**Write a function that takes an array of numbers and returns the sum of the numbers. 
    * The numbers can be negative or non-integer. If the array does not contain any 
    * numbers then you should return 0.
    * 
    */
   return numbers.length > 0 ? numbers.reduce((prev, cur) => prev + cur) : 0; 
};

sum([1, 5.2, 4, 0, -1])