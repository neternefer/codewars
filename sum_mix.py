def sum_mix(arr):
    """Given an array of integers as strings and numbers,
    return the sum of the array values as if all were numbers.
    """
    return sum([int(num)for num in arr])