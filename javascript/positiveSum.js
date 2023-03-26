function positiveSum(arr) {
    //Return sum of positive numbers in the array
    let sum = 0;
    arr.filter((a) => a > 0).map((e)=>sum+=e);
    return sum;
  }