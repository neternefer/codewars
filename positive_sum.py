def positive_sum(arr):
	'''Return the sum of all positives array items.
	If array is empty, return 0.
	'''
	
	return sum(item for item in arr if item > 0)
