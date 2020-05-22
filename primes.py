# a natural number, say N, is a prime number
# 		(iff) 
# N is greater than one and has no positive divisors besides one and itself

# is n prime?
def isPrime(n):														
	if n > 1:										# primes are greater than 1
		for j in range(2, n):								# iterate linearly from 2 to n-1
			if (n % j) == 0:							# if a divisor is found -> n isn't prime
				return False
		else:										# no divisor found -> n is prime
			return True
	else:											# n is less than or equal to one -> n isn't prime
		return False

# iterate through the natural numbers! 
def getNumbers(CAP):
	for i in range(1, CAP+1):								# iterate from 1 to CAP
		if isPrime(i):									# check if prime or not, print desired output, reloop
			print(str(i) + " -> " + str(i) + " prime")
		else:										# not prime -> composite
			print(str(i))

if __name__ == '__main__':									# main()
	#getNumbers(100)									# from 1 to hundo
	a = [1,2,3,4,5,6,7]
	for i in range(len(a)):
		print(a[i])
