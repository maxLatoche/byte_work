import math

def probability(iter_this):
	#sort array
	iter_this.sort()
	
	#check if array is odd or even
	#calculate median
	if (len(iter_this))%2 == 0:
		med = iter_this[int(len(iter_this)/2)]
	else:
		med = (iter_this[math.ceil((len(iter_this)/2))]+iter_this[math.floor((len(iter_this)/2))])/2
	print(med)

	#find average
	i = 0
	for val in iter_this:
		i += val
	avg = i/(len(iter_this)+1)
	print(avg)

	#find most common number
	checklist = []
	j = iter_this[0]
	for k in range(len(iter_this)+1):
		for val in iter_this:
			if val == j:
				checklist[k].append(j)
			elif val > j:
				j = val



some_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

probability(some_list)