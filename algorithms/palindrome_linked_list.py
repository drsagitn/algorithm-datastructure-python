"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseLList(self, node):
        pre = next_ = None
        cur = node
        while cur:
            next_ = cur.next
            cur.next = pre            
            pre = cur
            cur = next_
        return pre
    # Current: O(n) of time and O(1) of space
    # Alternative: push to a arr and check the reversed arr equal
    def isPalindrome(self, head: ListNode) -> bool:
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        low  = self.reverseLList(low)
        fast = head
        while low:
            if low.val != fast.val:
                return False
            low = low.next
            fast = fast.next
        return True

s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)
print(s.isPalindrome(node))