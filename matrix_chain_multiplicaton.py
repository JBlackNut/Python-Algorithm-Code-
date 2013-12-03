# this file is code for solving the matrix chain multiplication in chapter of book <Introduction to Algorithm>
# Problem Statement: in order to get well understand of dynamic problem, here we start from define the easy recursive call to solve the problem first

import numpy as np
def matrix_chain(P):
	"""
	Input:
		- P, should contain the size of each matrices, in the following format [(a, b), (c, d), ...]
	"""
	if isinstance(P, list): print "Input Error!"
	elif len(P) == 0 or len(P) == 1: print "Input variable length equal to zero"
	else:
		if len(P) == 2:
			return P[0][0] * P[0][1] * P[1][1]
		else:
			T, S = np.zeros((len(P), len(P))), np.zeros((len(P), len(P)))
			T.fill(np.inf)
			for l in range(2, n + 1):
				for i in range(0, n - l + 1):
					j = i + l - 1
					for k in range(i, j):
						q = T[i, k] + T[k + 1, j] + P[i][0] * P[k][1] * P[j][1]
						if q < T[i, j]:
							T[i, j] = q
							S[i, j] = k
		return T, S