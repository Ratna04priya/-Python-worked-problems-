# Max sub Array

from sys import maxint

def maxarray(a,n):
	b=[]
	start = -maxint - 1
	end = 0
	
	for i in range(0,n):
		end = end + a[i]
		if (start < end):
			start = end
			b.append(a[i])

	if end<0:
		end = 0
	m=len(b)
	for i in range(0,m):
		print b[i]
	return start

a=[]
k=int(input("Enter the number of inputs you want to give : "))
print("Now give the numbers")
for i in range(0,k):
	b=int(input())
	a.append(b)

maxarray(a,k)
	
