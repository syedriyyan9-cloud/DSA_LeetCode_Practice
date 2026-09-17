# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        s = head
        f = head
        output = []

        while s != None:
            if f is None or f.next is None:
                return s
            else:
                f = f.next.next
            s = s.next
