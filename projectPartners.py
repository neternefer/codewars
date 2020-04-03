#Mrs. Frizzle is beginning to plan lessons for her science class next semester,
#and wants to encourage friendship amongst her students.
#To accomplish her goal, Mrs. Frizzle will ensure each student
#has a chance to partner with every other student in the class
#in a series of science projects.
#Mrs. Frizzle does not know who will be in her class next semester,
#but she does know she will have n students total in her class.
#Create the function projectPartners with the parameter n
#representing the number of students in Mrs. Frizzle's class.
#The function should return the total number of unique pairs
#she can make with n students.
#Dont' use arrays.Input greater than or equal to 2.


def projectPartners(n):
    pairs = 0
    for p in range(1, n):
        pairs += (n - p)
    return pairs
