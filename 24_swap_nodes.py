from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first
        return second

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