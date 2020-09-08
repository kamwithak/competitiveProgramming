'''

Welcome! :)

 This is a toy program to print the approximated value of e ~ 2.17828
=>    1/(n!) + 1/((n-1)!) + 1/((n-2)!) + ... + 1/(3!) + 1/(2!) + 1/(1!) + 1/(0!) = e, as n -> inf

One-liner recursive programs:

'''

def e(n):
	def f(n):
		'''
		Version 1:
		@inactive
		'''
		# if n == 1 or n == 0:
		# 	return 1
		# else:
		# 	return (n * f(n-1))
		'''
		Version 2:
		@active
		'''
		return 1 if n <= 1 else n * f(n-1)

	'''
	Version 1:
	@inactive
	'''	
	# if n == 0:
	# 	return 1
	# else:
	# 	return 1/f(n) + e(n - 1)

	'''
	Version 2:
	@active
	'''	
	return 1 if n == 0 else 1/f(n) + e(n-1)

print(f"e is approximately {e(99)}")

def fibo(n):
	
	'''
	Version 1:
	@inactive
	'''
	# if n == 0 or n == 1:
	# 	return n
	# return fibo(n-2) + fibo(n-1)

	'''
	Version 2:
	@inactive
	'''
	# if n > 1:
	# 	return fibo(n-2) + fibo(n-1)
	# return n
	
	'''
	Version 3:
	@active
	'''
	return n if n <= 1 else fibo(n-1) + fibo(n-2)

# for i in range(10):
# 	print(fibo(i))
