from typing import Optional
import heapq
# --------merge-method---------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def merge2Lists(self, list1:list, list2:list) -> list:
#         dummy = ListNode()
#         tail = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#         tail.next = list1 if list1 else list2
#         return dummy.next
    
#     def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
#         for i in range(len(lists)-1):
#             lists[i+1] = self.merge2Lists(lists[i], lists[i+1])
#         return lists[len(lists)-1]
# ----------------------------------------------------------------------------------
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        heap = []
        counter = 0
        for lst in lists:
            if lst:
                heapq.heappush(heap,(lst.val,counter,lst))
                counter += 1
        while heap:
            val, _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap,(node.next.val,counter,node.next))
                counter += 1
            tail.next = node
            tail = tail.next
        return dummy.next
        


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
lists = [
    make_linked_list([1, 4, 5]),
    make_linked_list([1, 3, 4]),
    make_linked_list([2, 6])
]

# sanity check that it built correctly
for l in lists:
    print_linked_list(l)

print("Merged list:")
print_linked_list(Solution().mergeKLists(lists))