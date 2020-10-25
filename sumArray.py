def sumArray(arr):
    """Sum all the numbers of the array (in F# and Haskell you get a list) except the
    highest and the lowest element (the value, not the index!)."""
    if arr:
        return sum(sorted(arr)[1:-1])
    return 0