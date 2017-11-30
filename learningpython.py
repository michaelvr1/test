'''A module for demo exceptions.'''
def convert(s):
	'''Convert to int'''
	try:
		x = int(s)
	except (ValueError,TypeError):
		print("Wrong value bub")
		x= -1
	return x
