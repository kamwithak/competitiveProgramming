<<<<<<< HEAD
class MergeTwoArrays():
    def __init__(self, nums1, nums2, m, n):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n
    
    def merge(self):
        ans = []
        while (self.m > 0 and self.n > 0):
            if (self.nums1[0] < self.nums2[0]):
                ans.append(self.nums1[0])
                del self.nums1[0]
                self.m -= 1
            else:
                ans.append(self.nums2[0])
                del self.nums2[0]
                self.n -= 1
        while (self.m > 0):
            ans.append(self.nums1[0])
            del self.nums1[0]
            self.m -= 1
        while (self.n > 0):
            ans.append(self.nums2[0])
            del self.nums2[0]
            self.n -= 1
        return ans

    def mergeInPlace(self):
        pass

if __name__ == "__main__":
    obj = MergeTwoArrays([1,3,5,7], [0,2,4,6], 4, 4)
    print(obj.merge())
=======
class MergeTwoArrays():
    def __init__(self, nums1, nums2, m, n):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n
    
    def mergeUsingAdditionalSpace(self):
        ans = []
        while (self.m > 0 and self.n > 0):
            if (self.nums1[0] < self.nums2[0]):
                ans.append(self.nums1[0])
                del self.nums1[0]
                self.m -= 1
            else:
                ans.append(self.nums2[0])
                del self.nums2[0]
                self.n -= 1
        while (self.m > 0):
            ans.append(self.nums1[0])
            del self.nums1[0]
            self.m -= 1
        while (self.n > 0):
            ans.append(self.nums2[0])
            del self.nums2[0]
            self.n -= 1
        return ans

    def mergeWithoutUsingAdditionalSpace(self):
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = self.m-1
        p2 = self.n-1
        
        # Index i backwards through the array, each time writing
        # the largest value pointed at by p1 or p2.
        for i in range(self.n+self.m-1, -1, -1):
            # if (p2 < 0):
            #     break
            if (p1 >= 0 and self.nums1[p1] > self.nums2[p2]):
                self.nums1[i] = self.nums1[p1]
                p1 -= 1
            elif (p2 >= 0):
                self.nums1[i] = self.nums2[p2]
                p2 -= 1

        return self.nums1


if __name__ == "__main__":
    obj = MergeTwoArrays([1,3,5,7,None,None,None,None], [0,2,4,6], 4, 4)
    print(obj.mergeWithoutUsingAdditionalSpace())
>>>>>>> c87048f6d203a6448ef863b636a9fca7537a1dee
