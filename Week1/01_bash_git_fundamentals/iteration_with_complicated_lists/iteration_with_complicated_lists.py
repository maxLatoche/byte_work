complicated = [25, 36, ['Max', 'MAX_WELL'], [42, ['Jackie', 'Robinson']]]


for val in complicated:
	if type(val) == list:
		for i in val:
			print(i)
	else:
		print(val)