from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        dummy = ListNode(0)
        dummy.next=head
        s = f = dummy
        for _ in range(n):
            f = f.next
        while f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next
print(Solution().removeNthFromEnd([1,2,3,4,5], 2))