def odd_count(n):
    """Given a number n, return the number of positive odd numbers below n.
    oddCount(7) //=> 3, i.e [1, 3, 5]
    oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
    - Look at the top of the range: if it is odd then add 1, if even leave alone.
    - Look at the bottom of the range: if it is odd then subtract 1, if even leave alone.
    - Take the difference between the new even top and bottom; then divide by two.
    So for the range [1,100] you get 100−02=50 odd integers.
    """
    top = n - 1 if (n - 1) % 2 == 0 else n
    return top  // 2