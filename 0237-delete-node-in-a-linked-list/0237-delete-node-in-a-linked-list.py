# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur_node = node
        next_node = node.next
        cur_node.val = next_node.val
        cur_node.next = next_node.next
        del next_node
        