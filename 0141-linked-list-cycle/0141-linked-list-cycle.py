# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        while s is not None:
            if f is None or f.next is None:
                break
            else:
                f = f.next.next
                if f == s:
                    return True
                s = s.next
        return False