# this file is code for solve following problem
# problem state: given two input array or string, here assume give two input strings, S1 and S2, we want to find the most common sequence in the two string. s3 could be not consecutive character in two string

# solution: the basic concept in solve this kind of problem, is use dynamic programming, since the T(j) is related to its subproblem T(j - 1), and we could recursive call function to solve the similar subproblem

import numpy as np

def most_common_string(S1, S2):
	"""
	Input:
		- S1, the string contain the DNA sequence
		- S2, the string contain the DNA sequence
	Output:
		- S3, the string contain the most common suquence in the two given DNA sequence
	"""
	if isinstance(S1, str) and isinstance(S2, str):
		if len(S1) == 0 or len(S2) == 0: return None
		else:
			C = np.zeros((len(S1), len(S2)), dtype = np.int8)
			P = np.zeros((len(S1), len(S2)), dtype = str)
			for i in range(len(S1) - 1, 0):
				for j in range(len(S2) - 1, 0):
					if i == 0 or j == 0:	C[i, j] = 0
					else:	None
					if S1[i] == S2[j]:
						C[i, j] = C[i - 1, j - 1] + 1
					else:
						C[i, j] = max(C[i - 1, j], C[i, j - 1])
	else:
		return "Error! the input %s is not expected input type, please check it and try again!" %S1

# test set
