# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        while s is not None:
            if f is None or f.next is None:
                return None
            else:
                f = f.next.next
                s = s.next
                if f == s:
                    count = 0
                    node_set = set()
                    while head is not None:
                        if head in node_set:
                            return head
                        node_set.add(head)
                        # prev = head
                        head = head.next
