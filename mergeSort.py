class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addLast(self, node):
        cur = node
        while(cur.next != None):
            cur = cur.next
        cur.next = node
    
class MergeTwoLists():
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.ans = ListNode()

        self.merge(self.l1, self.l2)
    
    def getSize(self, LL):
        if (LL == None):
            return 0
        elif (LL.next == None):
            return 1
        else:
            ctr = 0
            cur = LL
            while (cur != None):
                ctr += 1
                cur = cur.next
            return ctr

    def getLastNode(self, LL):
        if (LL == None):
            return None
        elif (LL.next == None):
            return LL
        else:
            return self.getLastNode(LL.next)

    def getFirstNode(self, LL):
        if (LL == None):
            return None
        return LL

    def remove(self, firstNode):
        firstNode.next = None

    def merge(self, l1, l2):
        while (self.getSize(l1) > 0 and self.getSize(l2) > 0):
            if (self.getFirstNode(l1).val < self.getFirstNode(l2).val):
                self.ans.addLast(self.getFirstNode(l1))
            else:
                self.ans.addLast(self.getFirstNode(l2))
        while (self.getSize(l1) > 0):
            self.ans.addLast(self.remove(self.getFirstNode(l1)))
        while (self.getSize(l2) > 0):
            self.ans.addLast(self.remove(self.getFirstNode(l2)))
        return self.ans

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
    #l1 = ListNode(1, ListNode(2, ListNode(4)))
    #l2 = ListNode(1, ListNode(3, ListNode(4)))

    #obj = MergeTwoLists(l1, l2)
    #print(obj.getSize(l1))

    obj = MergeTwoArrays([1,3,5,7],[0,2,4,6],4,4)
    print(obj.merge())
    print(obj.mergeInPlace())
