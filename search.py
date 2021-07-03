subset = []

def generateSubsets(n, k=0):
    if (n == k):
        print(subset)
    else:
        generateSubsets(n, k+1)
        subset.append(k)
        generateSubsets(n, k+1)
        subset.pop()

if __name__ == "__main__":
    generateSubsets(3)