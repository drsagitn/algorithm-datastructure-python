"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
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
    
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        interval = 1
        while True:
            list_count = len(lists)
            if interval > list_count:
                break
            for i in range(0, list_count-interval, 2*interval):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *=2
        return lists[0] if list_count>0 else None
                
s = Solution()
inp = [[-1,1],[-3,1,4],[-2,-1,0,2]]
ret = []
for l in inp:
    dummy = ListNode(-1)
    head = dummy
    for item in l:
        dummy.next = ListNode(item)
        dummy = dummy.next
    ret.append(head.next)
print(s.mergeKLists(ret))