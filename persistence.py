import functools
def persistence(n):
    count = 0
    def recur(n, count):
        if n < 10:
            return 0
        else:
            result = functools.reduce(lambda x, y: int(x) * int(y), list(str(n)))
            while result >= 10:
                count += 1
                result = recur(result)
            return count
    return recur(n)