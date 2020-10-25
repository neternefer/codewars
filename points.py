def points(games):
    """Our football team finished the championship.
    The result of each match look like "x:y".
    Results of all matches are recorded in the collection.
    For example: ["3:1", "2:2", "0:1", ...]
    Write a function that takes such collection and counts the
    points of our team in the championship.
    Rules for counting points for each match:
    if x>y - 3 points
    if x<y - 0 point
    if x=y - 1 point
    """
	return sum([3 if score[0] > score[2] else 0 if score[0] < score[2] else 1 for score in games])