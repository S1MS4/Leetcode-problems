from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        curr = head
        prev = None
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = self.reverseKGroup(curr,k)
        return prev


def make_linked_list(values):
    """Build a linked list from a Python list, return head node."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals) if vals else "None")

# Test input: classic LeetCode example
lists = make_linked_list([1, 2, 3, 4])

# sanity check that it built correctly
print_linked_list(lists)

print(print_linked_list(Solution().reverseKGroup(lists, 3)))