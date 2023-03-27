function invert(array) {
    /**Given a set of numbers, return the additive inverse of each. 
     * Each positive becomes negatives, and the negatives become positives. */
    return array.length > 0 ? array.map((e) => e * (-1)) : [];
 }