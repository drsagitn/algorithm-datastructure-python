"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0        
        ret_node = ListNode(-1)
        head = ret_node
        while l1 is not None or l2 is not None:
            v1 = 0
            v2 = 0
            if l1 is not None:
                v1 = l1.val             
            if l2 is not None:
                v2 = l2.val 
            s = v1 + v2 + carry
            if s >= 10:
                carry = 1 
            else:
                carry = 0            
            ret_node.next = ListNode(s%10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            ret_node = ret_node.next
        if carry == 1:
            ret_node.next = ListNode(1)
        return head.next
            
s = Solution()
a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(3)
print(s.addTwoNumbers(a, b))