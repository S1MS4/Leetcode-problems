from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_list = ListNode()
        result_head = sum_list  # Keep a reference to the head of the result list
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            sum_list.val = carry % 10
            carry //= 10
            if l1 or l2 or carry:
                sum_list.next = ListNode()
                sum_list = sum_list.next
        return result_head
    
# example usage:
add = Solution()
result = add.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
while result:
    print(result.val, end=" -> ")
    result = result.next