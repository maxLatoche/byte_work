import re

def title_case(my_string, exceptions):
	caps_string = my_string.title()
	'''
	for i in caps_string:
		print(i)
		for j in exceptions:
			if i.lower() == j.lower():
				caps_string.replace(i, i.lower())
				print(caps_string)
	'''
	for i in range(0,len(exceptions)):
		if exceptions[i] in my_string:
			caps_string = caps_string.replace(exceptions[i], exceptions[i].lower())
	return caps_string


print(title_case("optimus prime and the autobots assembled to fight the decepticons", ['the', 'and', 'decepticons', 'to']))