# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
iterate over list, increment counter, identify the size of the list

ith node = size_of_list - n + 1

if (i = 1):
    # remove the last element
elif (i is between 1 and n exclusively):
    # remove middle
elif (i == n):
    # remove last element

"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size_of_list = 0
        curNode = head
        
        while (curNode != None):
            size_of_list += 1
            curNode = curNode.next
        
        node_for_deletion = size_of_list-n+1
        ctr = 1

        if (node_for_deletion == 1):
            return head.next
        
        elif (1 < node_for_deletion < size_of_list):
            curNode = head
            while (curNode != None):
                if (ctr == node_for_deletion-1):
                    curNode.next = curNode.next.next
                curNode = curNode.next
                ctr += 1
        
        elif (node_for_deletion == size_of_list):
            curNode = head
            while (curNode != None):
                if (ctr == node_for_deletion-1):
                    curNode.next = None
                curNode = curNode.next
                ctr += 1
        
        return head
