def odd_or_even(arr):
    """Given a list of numbers, determine whether the sum of its elements is odd or even.
    Give your answer as a string matching "odd" or "even".
    If the input array is empty consider it as: [0] (array with a zero).
    """
    return 'even' if sum(arr) % 2 == 0 or len(arr) == 0 else 'odd'