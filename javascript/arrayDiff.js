function arrayDiff(a, b) {
  /**
   * Subtract one list from another and returns the result.
     It should remove all values from list a, which are present in list b keeping their order.
   */

    return a.reduce((prev, cur) => b.includes(cur) ? prev : prev.concat(cur), []);
}

console.log(arrayDiff([1,2,2,2,3],[2]))