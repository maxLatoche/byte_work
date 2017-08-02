def fib(num):
	#create list with first value
	my_arr = [0]
	#instantiate variables with first 2 values
	a = 0
	b = 1
	#add each value to the last and update current values 
	#append each new value to the list
	while len(my_arr) < num:
		#add if statement to check 'even' requirement 
		if b % 2 == 0:
			my_arr.append(b)
		a, b = b, a+b
	#print each element in list
	for val in my_arr:
		print(val)

fib(10)