import re 

def is_palindrome(my_string):
	low_string = my_string.lower()
	read = re.findall(r'\w',low_string, re.I)
	return read == read[::-1]

print(is_palindrome("A Toyota's not a Toyota"))
print(is_palindrome("A Toyota's a Toyota"))