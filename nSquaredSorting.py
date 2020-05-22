def sum(lo, hi):
	if (lo > hi):
		return 0
	else:
		return lo + sum(lo + 1, hi)
		
def fib(n, computed = {0: 0 , 1: 1}):
	if n not in computed:
		computed[n] = fib(n-1, computed) + fib(n-2, computed)
	return computed[n]

#for i in range(0, 101):
#	print(str(i) + ':' + str(fib(i)))

def fact(n):
	if (n == 1): return 1.0
	else: return n * fact(n - 1)

def fastFact(n, m=1):
	if (n == 1): return m
	else: return fastFact(n-1, n*m)

#print(fact(2))

def baseToPower(a, b):
	if (b == 0): return 1
	elif (b == 1): return a
	else:
		tmp = baseToPower(a, b/2)
		if (b % 2 == 0): return tmp * tmp
		else: return a * tmp * tmp

#print(baseToPower(9,2))

def findRepeatedElementsInList(myList):							# O(n^2)
	repeatedElements = []
	steps = 0
	for i in range(0, len(myList)-1):
		for j in range(i+1, len(myList)):
			steps += 1
			if (myList[i] == myList[j]):
				repeatedElements.append(myList[i])
	print(steps)
	return repeatedElements

def findRepeatedElementsEfficiently(myList):
	_dict = {}
	tmp = []
	steps = 0
	for elem in myList:
		steps += 1
		if elem in _dict:
			_dict[elem] += 1
		else:
			_dict[elem] = 1
	'''
	for key in _dict:
		if (_dict[key] > 1):
			i = 0
			while (i < _dict[key]):
				steps += 1
				tmp.append(key)
				i += 1
	'''
	print(len(_dict))
	print(steps)
	#print(tmp)
	return _dict

def bubbleSort(arr):
	steps = 0
	for i in range(0, len(arr)-1):					# k to n-2
		for j in range(i+1, len(arr)):				# k+1 to n-1
			steps += 1
			if (arr[i] > arr[j]):
				arr[j], arr[i] = arr[i], arr[j]
	return arr

def selectionSort(arr):
	steps = 0
	for i in range(0, len(arr)-1):
		minIndex = i
		for j in range(i+1, len(arr)):
			#print('<' + str(i) + ',' + str(j) + '>')
			steps += 1
			if (arr[j] < arr[minIndex]):
				minIndex = j
		if (minIndex != i):
			arr[j], arr[minIndex] = arr[minIndex], arr[j]
	print(steps)
	return arr

def insertionSort(arr):
	steps = 0
	for j in range(1, len(arr)):
		while (j >= 1):
			steps += 1
			if (arr[j-1] > arr[j]):
				arr[j], arr[j-1] = arr[j-1], arr[j]
			j -= 1
	print(steps)
	return arr

_map = {"]" : "[", "}" : "{", ")" : "("}

def empty(stack):
    return (len(stack) == 0)

def peak(stack):
    return (stack[len(stack)-1])
	
def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

def balancedOrNot(myStr): 
    stack = [] 
    for i in myStr: 
        if i in _map.values(): 
            leftParanthesis = i
            stack.append(leftParanthesis)
        elif i in _map.keys():
            rightParanthesis = i 
            associatedLeftParanthesis = _map[rightParanthesis]
            if (not empty(stack) and (associatedLeftParanthesis == peak(stack))):
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
 

# Driver code 
#string = "{[]{()}}"
#print(string,"-", balancedOrNot(string)) 
  
#string = "{}[]{}[][[[]]]{}{}{}{}()"
#print(string,"-", balancedOrNot(string)) 

#myList = [5,4,3,23,24,23,423,4,3,4,3,-5,145,-324234,23,1]
#print(bubbleSort(myList))
#print(selectionSort(myList))
#print(insertionSort(myList))
#print(findRepeatedElementsInList(myList))
#print(findRepeatedElementsEfficiently(myList))