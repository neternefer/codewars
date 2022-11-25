def count_positives_sum_negatives(arr):
    """Given an array of integers, return an array,
    where the first element is the count of positive numbers and the
    second element is sum of negative numbers.
    If the input array is empty or null, return an empty array.
    [f(x) if condition else g(x) for x in sequence]"""
    if len(arr):
        positive = len(list(filter(lambda num: num > 0, arr)))
        negative = sum(list(filter(lambda num: num < 0, arr)))
        print(positive, negative)
    return []

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])