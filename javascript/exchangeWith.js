//Exchange the elements of two arrays in-place in a way 
//that their new content is also reversed.
function exchangeWith(a, b) {
    let copyB = [...b];
    let copyA = [...a];
    copyB.splice(0, b.length, ...copyA.reverse());
    a.splice(0, a.length,...b.reverse());
    return a, b;
  }