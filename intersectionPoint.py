"""
Given two straight line segments (represented as a start point and an end point),
compute the point of intersection, if any.
"""

def get_equation(arr1,arr2):
	x1,y1=arr1
	x2,y2=arr2
	m = (y2-y1)/(x2-x1)
	c = y1-m*x1
	return m,c

def is_on_segment(x,y,arr1,arr2):
	x1,y1=arr1
	x2,y2=arr2
	return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

def x_inter(arr1,arr2,arr3,arr4):
	m1,c1=get_equation(arr1,arr2)
	m2,c2=get_equation(arr3,arr4)
	try:
		x = (c2-c1)/(m1-m2)
		y = m1*x+c1
		if is_on_segment(x,y,arr1,arr2) and is_on_segment(x,y,arr3,arr4):
			return x,y
		else:
			print('Not on segment')
	except ZeroDivisionError:
		print('No intercept')
	

arr1,arr2,arr3,arr4 = [1,1],[2,2],[-1,1],[0,4]
print(x_inter(arr1,arr2,arr3,arr4))

arr1,arr2,arr3,arr4 = [0,1],[1,1],[0,3],[1,3]
print(x_inter(arr1,arr2,arr3,arr4))

# import matplotlib.pyplot as plt
# plt.plot([-10,2],[10,20])
# plt.plot([-1,0],[10,40])
# plt.plot([-0.7428571428571428],[17.714285714285715], 'rx')
# plt.show()

arr1,arr2,arr3,arr4 = [-10,10],[2,20],[-1,10],[0,40]
print(x_inter(arr1,arr2,arr3,arr4))