//Create a program that returns true if the sum of the squares 
//of each element in a is strictly greater than the sum of the 
//cubes of each element in b.
function arrayMadness(a, b) {
    return (a.reduce((acc, el) => acc + el**2) > b.reduce((acc, el) => acc + el**3));
  }