# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        cur = head
        values = []
        while cur != None:
            values.append(cur.val)
            cur = cur.next
        dup = values[:]
        dup.reverse()
        return values == dup
