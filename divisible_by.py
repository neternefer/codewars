def divisible_by(numbers, divisor):
    """Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
    First argument is an array of numbers and the second is the divisor.
    """
    return [num for num in numbers if num % divisor == 0]