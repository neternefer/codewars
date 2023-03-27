function countPositivesSumNegatives(input) {
    /**
     * Return an array, where the first element is the count of positives numbers
     * and the second element is sum of negative numbers. 0 is neither positive nor negative.

        If the input is an empty array or is null, return an empty array.
    */
    return  input != null && input.length > 0 ? [input.filter((a) => a > 0).length, input.filter((a) => a < 0).reduce((prev, cur) => prev + cur)] : [];
  }

  countPositivesSumNegatives(null)