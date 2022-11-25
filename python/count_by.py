def count_by(x, n):
    """
    Create a function with two arguments that will return an array of
    the first (n) multiples of (x).
    count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
    count_by(2,5) #should return [2,4,6,8,10]
    Fun solution:
    return range(x, x * n + 1, x)
    """
    return [x * i for i in range(1, n + 1)]