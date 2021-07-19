# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # curNodeA = headA
        # while (curNodeA):
        #     curNodeB = headB
        #     while (curNodeB):
        #         if (curNodeA == curNodeB != None):
        #             return curNodeA
        #         curNodeB = curNodeB.next                
        #     curNodeA = curNodeA.next
        # return 0
        
        _set = set()
        curNodeA = headA
        while (curNodeA):
            _set.add(curNodeA)
            curNodeA = curNodeA.next
        curNodeB = headB
        while (curNodeB):
            if (curNodeB in _set):
                return curNodeB
            curNodeB = curNodeB.next
        return None