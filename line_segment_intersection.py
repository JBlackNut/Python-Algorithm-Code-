# author 	: jianbin.hong.cn@gmail.com
# date		: 2015/10/13

import sys

class Street(object):
	"""
	"""
	start_point = None
	end_point 	= None
	points 		= None

	def __init__(self, points):
		"""
		Assume each street have more than two points
		"""
		assert type(points) is list
		assert len(points) > 1
		assert type(points[0]) is tuple

		self.start_point = points[0]
		self.end_point = points[-1]
		self.points = points

	def _intersect_with_another_street(self, another_street):
		"""
		"""

		def det(A, B):
			"""
			"""
			return A[0] * B[1] - B[0] * A[1]

		assert type(another_street) is Street
		intersection_point = set()
		for i in range(1, len(self.points)):
			A1 = self.points[i - 1]
			A2 = self.points[i]

			for j in range(1, len(another_street.points)):
				B1 = another_street.points[j - 1]
				B2 = another_street.points[j]

				diff1 	= (B1[0] - A1[0], B1[1] - A1[1])

				r 		= (A2[0] - A1[0], A2[1] - A1[1])
				s 		= (B2[0] - B1[0], B2[1] - B1[1])
				rs		= det(r, s)

				if rs == 0: continue
				t 		= (det(diff1, s)) * 1.0 / rs
				u 		= (det(diff1, r)) * 1.0 / rs
				if u >= 0 and u <= 1 and t >= 0 and t <= 1: 
					point = (A1[0] + t * r[0], A1[1] + t * r[1])
					intersection_point.add(point)

		if len(intersection_point):
			return True, intersection_point

		return False, None

if __name__ == "__main__":
	a = Street([(1, -2), (2, -1), (6, 0)])
	b = Street([(2, -2), (2, 2)])
	c = Street([(-2, 0), (6, 2)])
	d = Street([(4, -2), (4, 2)])
	e = Street([(5, -1), (5, 2)])
	print a._intersect_with_another_street(b)
	print a._intersect_with_another_street(c)
	print a._intersect_with_another_street(d)
	print a._intersect_with_another_street(e)
