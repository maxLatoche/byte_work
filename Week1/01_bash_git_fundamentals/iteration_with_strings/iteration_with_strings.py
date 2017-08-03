def reverse_my_string(str):
	split_str = list(str) 
	split_str.reverse()
	reversed_str = "".join(split_str)
	print(reversed_str)

reverse_my_string("maxlatoche")