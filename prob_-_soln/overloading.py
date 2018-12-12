# Python overloading

import math

n=int(input("Select 0 for easy and 1 for tough"))
if n==0:
	a=12
	b=18
	print (a+b)

	x="Hello"
	z=" "
	y="Imon !"
	print(x+z+y)

if n==1:
	class point:
		
		def __init__(self,x,y):
			self.x=x
			self.y=y


		def __add__(self,other):
			return point(self.x + other.x, self.y + other.y)

		def __str__(self):
			string = str(self.x)
			string = string + "," + str(self.y)
			return string
	
	point1 = point(6,5)
	point2 = point(1,-2)
	point3 = point1 + point2
	print(point3)

