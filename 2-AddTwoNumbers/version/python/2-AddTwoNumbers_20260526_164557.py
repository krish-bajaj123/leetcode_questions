# Last updated: 5/26/2026, 4:45:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        curr = dummy
10        carry = 0
11
12        while l1 or l2 or carry:
13            val1 = l1.val if l1 else 0
14            val2 = l2.val if l2 else 0
15
16            total = val1 + val2 + carry
17            carry = total // 10
18            curr.next = ListNode(total % 10)
19
20            curr = curr.next
21            if l1: l1 = l1.next
22            if l2: l2 = l2.next
23
24        return dummy.next
25        