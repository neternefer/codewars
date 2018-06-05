def nth_smallest(arr, pos):
	s = sorted(arr, reverse=True)
	return s[-pos]
    
