import re

def my_func(str):
	new_str = re.sub(r'([a-z])\1+',r'\1',str)
	print(new_str)


string = "aabbccddeded"
my_func(string)