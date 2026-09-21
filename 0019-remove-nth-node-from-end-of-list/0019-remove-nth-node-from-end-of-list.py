# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:   
        ptr = head
        length = 0
        values = []
        while ptr:
           values.append(ptr.val)
           ptr = ptr.next
           length += 1

        if n == length:
            return head.next
        
        cur = head
        prev = cur
        value = values[-n]
        node_len = length - n
        count = 0
        while cur:
            if cur.val == value and count == node_len:
                prev.next = cur.next
            prev = cur
            cur = cur.next
            count += 1
            
        return head
            