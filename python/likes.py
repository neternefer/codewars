def likes(names):
    """
    Implement the function which takes an array containing the names of people that like an item.
    It must return the display text as shown in the examples:

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    """
    match len(names):
            case 0:
                return "no one likes this"
            case 1:
                return f"{names[0]} likes this"
            case 2:
                return f"{names[0]} and {names[1]} like this"
            case 3:
                return f"{names[0]}, {names[1]} and {names[2]} like this"
    if len(names) >= 4:
            return f"{names[0]}, {names[1]} and {str(len(names) - 2)} others like this"
    
