def array_diff(a, b):
	'''Implement a difference function, which subtracts one list 
	from another and returns the result.
	It should remove all values from list a, which are present in list b.
	If a value is present in b, all of its occurrences must be removed from the other.
	'''
	new = [x for x in a if x not in b]
	return new
		
	

