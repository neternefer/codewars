#Return the inputted numerical
#year in century format. For example 2014, would return 21st.

def whatCentury(year):
    if year % 4 == 0 and year %100 == 0 and year % 400 == 0:
        century = int(year / 100)
    else:
        century = int(year / 100) + 1
    result = ""
    firsts = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
    seconds = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92]
    thirds = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
    
    if century in firsts:
        result = str(century) + "st"
    elif century in seconds:
        result = str(century) + "nd"
    elif century in thirds:
        result = str(century) + "rd"
    else:
        result = str(century) + "th"
    
    return result
