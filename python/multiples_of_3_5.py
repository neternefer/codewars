def solution(number):
	'''Returns the sum of all the multiples of 3 or 5 below the number 
	passed in.
	Note: If the number is a multiple of both 3 and 5, only count it once.
	'''
	
	return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
			

