# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value_list = []
        while head is not None:
            value_list.append(head.val)
            head = head.next

        l, r = 0 , len(value_list) - 1
        while l < r:
            if value_list[l] != value_list[r]:
                return False
            l += 1
            r -= 1
        return True