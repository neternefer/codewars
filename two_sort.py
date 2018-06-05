def two_sort(array):
	'''You will be given an vector of string(s). 
	You must sort it alphabetically (case-sensitive!!) and then return
	the first value.
	The returned value must be a string, and have "***" between each of 
	its letters.
	'''
	return "***".join(sorted(array)[0])
	
	
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]))
		
	
