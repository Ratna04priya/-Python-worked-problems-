# Inheritance - Shapes



import math

class Shape(object):
    
    def area(self):
        
        pass

  

class Square(Shape):
 
    def __init__(self, side_length):
        self.side = side_length

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*(self.side)

   
class Rectangle(Shape):
  
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

class Circle(Shape):
   
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return math.pi*2*self.radius

class Triangle(Shape):
    
    def __init__(self,s,ss,base,perpend):
	self.sideA=s
	self.sideB=ss
	self.base=base
	self.per=perpend

    def area(self):
	return (1/2)*bbase*per
  
    def perimeter(self):
	return sideA+sideB+bbase


   
def main():
	n=int(input("Enter youe choice:\n 1.Area for Rectangle\n 2.Area for Square\n 3.Area for Circle\n4.Area for Triangle\n"))
	if n==1:
		a=int(input("Enter the length"))
		b=int(input("Enter the width"))
		rect = Rectangle(a, b)
		print("Rectangle\n")
		print("  Area: " + str(rect.area()))
		print("  Perimeter: " + str(rect.perimeter()))
		
	if n==2:
		k=int(input("Enter the side"))
		square = Square(k)
		print("Square\n")
		print("  Area: " + str(square.area()))
		print("  Perimeter: " + str(square.perimeter()))

	if n==3:
		m=int(input("Enter the radius"))
		circle = Circle(m)
		print("Circle\n")
		print("  Area: " + str(circle.area()))
		print("  Perimeter: " + str(circle.perimeter()))
		

	if n==4:
		x=int(input("Enter the side1"))
		y=int(input("Enter the side2"))
		z=int(input("Enter the base"))
		l=int(input("Enter the perpendicular to base"))
		triangle = Triangle(x,y,z,l)
		print("Triangle\n")
		print("  Area: " + str(triangle.area()))
		print("  Perimeter: " + str(triangle.perimeter()))
		


if __name__ == '__main__':
	main()
