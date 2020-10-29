def divisors(n):
    """Count the number of divisors of a positive integer n.
    Random tests go up to n = 500000.
    """
    count = 0
    i = 1
    while i <= n :
        if (n % i==0) :
            count += 1
        i = i + 1
    return count