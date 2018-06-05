#1.find all divisors of a number
import math
def find(num):
    d = list(filter(lambda x: (num % x == 0), range(1, num + 1)))
    sq = list(map(lambda x: x * x, d))
    s = sum(sq)
  
    if square(s):
        return [num, s]
        
#2.Check if num is a perfect square
def square(n):
    x = n // 2
    y = set([x])
    if x == 0:
        return 1
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y:
            return False
        y.add(x)
    return True
    
#3.Put it together
def list_squared(m, n):
    result = []
    for number in range(m, n + 1):
        if find(number) != None:
            result.append(find(number))
    #print(result)   
    return result
#-----------------------------------------------------------------
import math
def find(num):
	l1 = []
	divs = sum([i * i for i in range(1, num // 2 + 1) if num % i == 0]) + num * num
	if round(math.sqrt(divs)) == math.sqrt(divs):
		l1.append(num)
		l1.append(divs)
		
	return l1
def list_squared(m, n):
	result = []
	num = 0
	if m == 1:
		result.append([1, 1])
	else:
		num = m
		if find(i) != []:
			result.append(find(num))
	for i in range(m + 1, n + 1):
		if find(i) != []:
			result.append(find(i))
		
	return result
	
#-------------------------------------------------------------------
#Most effective
from math import sqrt, ceil

def list_squared(m, n):
	'''To find all divisors of a given number n, 
	you need only check up to the square root of n,
	for i in range(1, int(sqrt(n)) + 1):. 
	All the divisors greater than sqrt(n) can then be found by doing n // i.
	'''
	result = []
	for i in range(m, n):
		divs = 0
		for j in range(1, ceil(sqrt(i))):
			#checking divisors till sqrt(num)
			#getting smaller divisors
			if i % j == 0:
				divs += j * j
				if i != 1:
					#getting larger divisors
					divs += (i // j) ** 2
		if i == 1:
			divs = 1
		if round(sqrt(divs)) == sqrt(divs):
			result.append([i, divs])
	
		
	return result



            
