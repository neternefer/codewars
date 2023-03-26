function sumTwoSmallestNumbers(numbers) {  
    //Sum two smallest numbers in array
    let sum = 0;
    numbers.sort((a,b) => a - b).slice(0, 2).map((e) => sum += e);
    return sum;
  }

  sumTwoSmallestNumbers([19, 5, 42, 2, 77]) //7