function squareSum(numbers){
    // Square each number and then sum the results together.
    let sum = 0;
    numbers.map((e) => e ** 2).map((f) => sum += f);
    return sum;
  }

  squareSum([1, 2, 2])