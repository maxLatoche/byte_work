import math

def probability(iter_this):
	#sort array
	iter_this.sort()
	print(iter_this)
	
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
	#create empty dict
	counter = {}
	for j in iter_this:
		if j in counter:
			#dict count goes up for each time value is encountered
			counter[j] += 1
		else:
			#each value in array becomes key
			counter[j] = 1

	most_common = 0
	#iterate through counter to find largest value
	for k in counter:
		if counter[k] > most_common:
			most_common = k
	print(most_common)

some_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

probability(some_list)