def is_palindrome(str):
	str_list = list(str)
	str_list.reverse()
	rev_str = "".join(str_list)
	if str == rev_str:
		return True
	else:
		return False
	


print(is_palindrome("max"))
print(is_palindrome("tacocat"))