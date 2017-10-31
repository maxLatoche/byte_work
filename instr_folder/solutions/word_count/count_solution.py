# check out the "with" statement with get rid of try and finally

import operator
# Gets all words and their occurencies in a dictionary
def word_stats(filename, n):
	file_words = dict()

	with open(filename) as f:
	
		words = f.read().split(" ")
	
		for word in words:
			if word in file_words:
				file_words[word] += 1
			else:
				file_words[word] = 1

	new_list = dict(sorted(file_words.items(), key=operator.itemgetter(1),reverse=True)[:5])
	return new_list
print(word_stats("article.txt", 5))


