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