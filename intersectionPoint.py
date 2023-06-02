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


def x_inter(arr1,arr2,arr3,arr4):
	m1,c1=get_equation(arr1,arr2)
	m2,c2=get_equation(arr3,arr4)
	try:
		x = (c2-c1)/(m1-m2)
		y = m1*x+c1
		return x,y
	except ZeroDivisionError:
		print('No intercept')
	

arr1,arr2,arr3,arr4 = [1,1],[2,2],[-1,1],[0,4]
print(x_inter(arr1,arr2,arr3,arr4))

#import matplotlib.pyplot as plt
#plt.plot([-2,1,2],[-2,1,2])
#plt.plot([-2,-1,0],[-2,1,4])
#plt.plot([-2],[-2], 'rx')
#plt.show()

arr1,arr2,arr3,arr4 = [0,1],[1,1],[0,3],[1,3]
print(x_inter(arr1,arr2,arr3,arr4))