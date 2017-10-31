# Python in keyword to check for value in the list

# Instead of trying to think how to write a code to check a number by the sums of 6 9 and 20
# We can just check the numbers as a sequence while always subtracting either 6 or 9 or 20
# We can check these numbers against a given list. For example 6-0 = 0 and 6 gets added to the list, then 12-6 = 6 and 12 gets added to the list. They both pass the check. 

# declare your lists
# You have to have zero in the list to make sure the first 6, 9, and 20 get added to the list
nugget_num = [0] 
not_nugget = []

# declare your number counter and success counter
# success will constantly increment until it reaches 6. After 6 mcnugget numbers in a row then every number will be a mcnugget number
count = 1
success = 0

while success < 6:
	if (count-6 in nugget_num) or (count-9 in nugget_num) or (count-20 in nugget_num):
		nugget_num.append(count)
		success += 1
		if success == 6:
			print("Every number after {} will be mcnugget numbers".format(count-6))
			break
	else:
		print("{} is not mcnugget".format(count))
		success = 0
	count +=1






















