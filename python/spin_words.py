def spin_words(sentence):
    """Write a function that takes in a string of one
    or more words, and returns the same string, but with
    all five or more letter words reversed .
    """
    return " ".join([word if len(word) < 5 else word[::-1] for word in sentence.split()])