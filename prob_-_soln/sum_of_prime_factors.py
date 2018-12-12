# Sum of all prime factors of a number


def isprime(n):
	
	if n<=1:
		return False
	if n<=3:
		return True

	if n % 2 == 0 or n % 3 ==0:
		return False
	i=5
	while i*i < n:
		if(n % i==0 or n % (i+2) ==0):
			return False
		i=i+6
	return True


def sumprime(a):
	s=0
	for i in range(1,a):
		if a % i == 0:
			if isprime(i):
				s=s+i
	return s



a= int(input("Enter the number"))
k=sumprime(a)

print("The sum of prime numbers is :",k)
