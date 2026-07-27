# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        d = ListNode(0,head)
        prev = d
        curr = head
        while curr:
            if curr.val in s:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return d.next