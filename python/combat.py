def combat(health, damage):
	'''
	Create a combat function that takes the player's current health 
	and the amount of damage recieved, and returns the player's new health. 
	Health can't be less than 0.
	'''
	if health - damage > 0:
		return health - damage
	return 0
	
#---------------------------------------------------------------------
#Clever:
def combat(health, damage):
	#if the result is negative, zero is returned correctly
	return max(0, health - damage)
