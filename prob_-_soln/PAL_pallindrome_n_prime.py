# Getting all PAL : Prime and pallindrome numbers between two given numbers




def pallindrome(n):
	temp=n
	rev=0
	while(n>0):
		dig = n % 10
		rev=rev*10 +dig
		n = n/10

	if temp == rev:
		return True
	else:
		return False

def isprime(n):
	if n<=1:
		return False
	if n<=3:
		return True

	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i*i < n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i=i+6
	return True

a=int(input("Enter the number of lower range "))
b=int(input("Enter the number of upper range "))

for i in range(a,b):
	if pallindrome(i) and isprime(i):
		print(i)

