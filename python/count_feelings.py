def count_feelings(st, arr):
    """
    You have two arguments: string - a string of random letters(only lowercase)
    and array - an array of strings(feelings).
    Your task is to return how many specific feelings are in the array.
    Example:
    string -> 'yliausoenvjw'
    output -> '3 feelings.' // 'awe', 'joy', 'love'
    """

    count = 0

    for feeling in arr:
        flag = True
        for letter in feeling:
            if letter not in st or feeling.count(letter) > st.count(letter):
                flag = False
        if flag:
            count+= 1
    return f"{count} feelings." if count > 1 else f"{count} feeling."



