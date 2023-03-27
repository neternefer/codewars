function digitize(n) {
    /*Given a random non-negative number, you have to return 
    the digits of this number within an array in reverse order.*/
    return n.toString().split('').reverse().map(Number);

}

digitize(35231)