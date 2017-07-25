import re

def word_stats(filename, n):
	#create list
	my_list = []
	#create dict
	my_dict = {}
	#open file with fileIO keywords
	with open(filename) as fp:
		#read file and send each word to list
		for line in fp:
			words = re.findall(r'\w+', line)
			my_list.extend(words)
	#iterate through list and assign each new word as a key, each duplicate increases value of key by 1
	for val in my_list:
		if val in my_dict:
			my_dict[val] += 1
		else:
			my_dict[val] = 1
	#sort dict by descending value
	sorted_dict = sorted(my_dict.items(), key= lambda x: x[1], reverse = True)
	#return top n values
	for i in range(0,n):
		print("\""+sorted_dict[i][0]+"\""+", "+str(sorted_dict[i][1]))


word_stats("../../../jng_instr_folder/week1/02_dict_datetime_fileIO/exercises/word-count/article.txt", 10)