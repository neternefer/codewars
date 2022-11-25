def adjacent_element_product(array):
	'''Find largest product of adjacent elements.'''
	#Product of first two elements
	first = array[0] * array[1]
	product = first
	for i in range(len(array)- 1):
		first =  array[i] * array[i + 1]
		
		if (first  > product):
			product = first 
	return product
	
def adjacent_element_product(array):
	return max(a * b for a, b in zip(array, array[1:]))

