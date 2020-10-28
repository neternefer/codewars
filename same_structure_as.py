from collections.abc import Iterable

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, str):
            yield from flatten(el)
        else:
            yield el

def same_structure_as(original,other):
    """Complete the function to return True when its argument is an array
    that has the same nesting structures and same corresponding length of
    nested arrays as the first array.
    """
    if isinstance(original, list) and isinstance(other, list):
        if len(list(flatten(original))) == len(list(flatten(other))):
            for arr1, arr2 in zip(original, other):
                return len(list(str(arr1))) == len(list(str(arr2))) or type(arr1) == type(arr2)
            return False
    return False