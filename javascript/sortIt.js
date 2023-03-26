function sortIt(arr){
    /**Sort numbers according to the number of occurances ASC
     * and DESC if that number is the same
     */
    let result = arr.slice();
    let countItems = (arr, val) => {
      var filtered = arr.filter((e)=> {return e == val;});
      return filtered.length;
     }
    result.sort(function(a, b) {
      if(countItems(arr, a) > countItems(arr, b)) {
        return 1;
      }
      if(countItems(arr, a) < countItems(arr, b)) {
        return -1;
      }
      if(countItems(arr, a) == countItems(arr, b) && a > b) {
        return -1;
      }
      if(countItems(arr, a) == countItems(arr, b) && a < b) {
        return 1;
      }
    }) 
    return result;
  }

  /**sortIt([1,1,1,2,2,2,3,3,3]) should return [3,3,3,2,2,2,1,1,1]
because number of 3,2 and 1 both are three, then according to 3>2>1 */

//   sortIt([1,1,1,2,2,3])
  sortIt([1,1,1,2,2,2,3,3,3])