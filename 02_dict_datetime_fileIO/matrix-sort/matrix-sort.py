import numpy as np

def matrix_ops(file_name):
	# access file
	with open(file_name) as fp:
		# read lines
		l = fp.readlines()
		# iterate over list and convert strings to numbers
		for i in range(0,len(l)):
			l[i] = l[i].split(" ")
			for j in range(0,len(l[i])):
				l[i][j] = int(l[i][j])
		#print(l)
		# send list to array
		x = np.array(l)
		print(x)
		

matrix_ops("../../../jng_instr_folder/week1/02_dict_datetime_fileIO/exercises/matrix-sort/testmatrix.txt")