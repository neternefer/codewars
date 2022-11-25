def warn_the_sheep(queue):
    """If the wolf is the closest animal to you, return
    "Pls go away and stop eating my sheep".
    Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
    where N is the sheep's position in the queue.
    """
    if queue[-1] == 'wolf':
        return "Pls go away and stop eating my sheep"
    return "Oi! Sheep number " + str(queue[::-1].index('wolf')) + "! You are about to be eaten by a wolf!"