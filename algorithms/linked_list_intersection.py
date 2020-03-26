"""
Write a program to find the node at which the intersection of two singly linked lists begins.
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m = headA
        n = headB
        sm = 0
        sn = 0
        while m and n:
            if m == n:
                return n
            if m.next is None and sm == 0:
                m = headB
                sm = 1
            else:
                m = m.next
            if n.next is None and sn == 0:
                n = headA
                sn = 1
            else:
                n = n.next            
        return None