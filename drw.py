def bubbleSort1(arr):
    steps = 0
    for i in range(0, len(arr)-1):					# k to n-2
        for j in range(i+1, len(arr)):				# k+1 to n-1
            steps += 1
            if (arr[i] > arr[j]):
                arr[j], arr[i] = arr[i], arr[j]
        print(arr)
    return arr

def bubbleSort2(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n-1):
            print(f"pairs being examined: {arr[i], arr[j]}")
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubbleSort1([9,8,7,6,5,4]))
