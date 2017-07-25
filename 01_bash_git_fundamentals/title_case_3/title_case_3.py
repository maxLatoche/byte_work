def titlecase(string, emph):
	my_string = string
	for i in range(0,len(emph)):
		if emph[i] in string:
			my_string = my_string.replace(emph[i],emph[i].upper())
	return my_string

print(titlecase("optimus prime and the autobots assembled to fight the decepticons",['optimus', 'prime', 'autobots', 'victorious']))