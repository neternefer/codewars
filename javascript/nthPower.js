function index(array, n){
    //find the N-th power of the element in the 
    //array with the index N. If N is outside of 
    //the array, then return -1
    if(array.length <= n){
      return -1;
    }
    return Math.pow(array[n], n);
  }