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
#
#
#
#
#