#Write a program that among the given numbers finds one that is different
#in evenness, and return a position of this number.
#example:iq_test("2 4 7 8 10") => 3 //
#Third number is odd, while the rest of the numbers are even



def iq_test(numbers):
    first_list = []
    second_list = []
    num_list = []
    for i in numbers.split(" "):
        num_list.append(i)
        if int(i)% 2 == 0:
            first_list.append(i)
        else:
            second_list.append(i)
    if len(first_list) == 1:
        return num_list.index(first_list[0]) + 1
    else:
        return num_list.index(second_list[0]) + 1
