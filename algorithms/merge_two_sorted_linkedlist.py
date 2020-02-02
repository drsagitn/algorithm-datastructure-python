"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while l1 is not None or l2 is not None:
            if l1 is None:
                dummy.next = l2
                l2 = l2.next
            elif l2 is None:
                dummy.next = l1
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    dummy.next = l2
                    l2 = l2.next
                else:
                    dummy.next = l1
                    l1 = l1.next
            
            dummy = dummy.next
        return head.next
                    