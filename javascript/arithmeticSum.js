/*Return the sum of the first (n) elements of a sequence
in which each element is the sum of the given integer (a),
and a number of occurences of the given integer (r), based
on the element's position within the sequence.
Read more about it
*/
function ArithmeticSequenceSum(a, r, n) {
  return n / 2 * (2 * a + (n - 1) * r);
}