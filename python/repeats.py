def repeats(arr):
    """In this Kata, you will be given an array of numbers in which
    two numbers occur once and the rest occur only twice. Your task
    will be to return the sum of the numbers that occur only once."""
    return sum([el for el in arr if arr.count(el) == 1])