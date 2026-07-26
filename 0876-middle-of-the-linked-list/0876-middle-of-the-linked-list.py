# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse the list
        count = 0
        h1 = head
        while head is not None:
            count += 1
            head = head.next
        if count % 2 == 0:
            count /= 2
            count = math.ceil(count)
            count += 1
        else:
            count /= 2
            count = math.ceil(count)
        while h1 is not None and (count - 1) != 0:
            h1 = h1.next
            count -= 1
        return h1
        