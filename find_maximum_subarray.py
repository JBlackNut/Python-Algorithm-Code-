# this file is code for solving the maximum subarray problem in python
# the basic code idea here is to solve it using divider and conquer, the main thing is to find the maximum value to
# go through the mid point of array

def find_maximum_subarray(A, low, high):
	"""
	"""
	if low == high:	return sum(A)
	else:
		middle_indice = (high - low) / 2
		(left_max, left_low, left_high) = find_maximum_subarray(A, low, middle_indice)
		(right_max, right_low, right_high) = find_maximum_subarray(A, middle_indice, high)
		(left_right_max, low_ind, high_ind) = across_maximum_subarray(A, low, high)
		if left_max >= right_max and left_max >= left_right_max:
			return (left_max, left_low, left_high)
		elif right_max >= left_max and right_max >= left_right_max:
			return (right_max, right_low, right_high)
		elif left_right_max >= left_max and left_right_max >= right_max:
			return (left_right_max, low_ind, high_ind)
		else:
			return "error in find_maximum_subarray function!"

def across_maximum_subarray(A, low, high):
	"""
	"""
	middle_indice = (high - low) / 2
	left_sum, right_sum = A[middle_indice], A[middle_indice + 1]
	sum_left, sum_right = 0, 0
	left_ind, right_ind = middle_indice, middle_indice + 1
	for i in range(middle_indice, low, -1):
		sum_left += A[i]
		if sum_left > left_sum:
			left_ind = i
			left_sum = sum_left
		else: None
	for j in range(middle_indice + 2, high, 1):
		sum_right += A[j]
		if sum_right > right_sum:
			right_ind = j
			right_sum = sum_right
	return (left_sum, right_sum, sum_right + sum_left)