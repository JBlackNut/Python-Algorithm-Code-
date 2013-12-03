# this file is code for the rod problem
# problem statement:
	# given a length n, rod, we could cut the rod in any we like. Obviously, it should in int size, and we also get the price of each size rods. Our goal is to compute the max revenue we could get by cutting the rod.

# author: Jianbin hong
# Date: 15/11/2013

import numpy as np
def rod_problem_solving(rod_n, price_n):
	"""
	Input:
		- rod_n: the length of rod
		- price_n: the prices of array
	Output:
		- the max revenue
	"""
	if isinstance(rod_n, int):	print "Error, the input %s is not expected type" % rod_n
	else:	None
	if rod_n == 0:	return "Error! input %s " %rod_n
	else:
		T = np.array((len(rod_n), len(rod_n)))
		price_n = [0.0].extend(price_n)
		for i in range(1, rod_n + 1):
			for k in range(0, i + 1):
				T[i, k] = price_n[k] + max(T[i - 1, :])
		return max(T[n, :])
