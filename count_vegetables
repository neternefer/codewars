
def count_vegetables(s):
    """(str) ->lst
    Return a list of tuples with the count of each vegetable in descending order.
    If there are any non vegetables mixed in discard them. If
    the count of two vegetables is the same sort in descending alphabetical order.
    
    >>> count_vegetables('potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage')
    [(2, 'tofu'),
       (2, 'potato'),
       (2, 'cucumber'),
       (2, 'cabbage'),
       (1, 'turnip'),
       (1, 'pepper'),
       (1, 'onion'),
       (1, 'mushroom'),
       (1, 'celery'),
       (1, 'carrot')]
    """
    veg_list = ["cabbage", "carrot", "celery",
                "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    tuple_list = []
    #String to list
    l = s.split()
    #Discard non-vegetables
    val = []
    for item in l:
        if item not in veg_list:
            l.remove(item)
        else:
            ct = l.count(item)
            tpl = (ct, item)
            if tpl not in tuple_list:
               tuple_list.append(tpl)
            if ct not in val:
               val.append(ct)
    #Find all tuples with particular number and sort this list by second tuple element.
    #Create list of lists
    alph = []
    for v in val:
        b = [item for item in tuple_list if v in item]
        alph.append(sorted(b, key=lambda tup: tup[1], reverse=True))
    #List of lists merged into one list
    #Tuple list sorted in descending order by first tuple element
    result = sorted(sum(alph, []), key=lambda tup: tup[0], reverse=True)
    
    return result
