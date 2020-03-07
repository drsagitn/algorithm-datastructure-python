"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head        
        n = head
        prev = None
        _next = None
        while n:
            _next = n.next
            n.next = prev
            prev = n
            n = _next
        return prev
            
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        rhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rhead

s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
s.reverseList(node)