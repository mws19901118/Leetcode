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
        node.val = node.next.val    #We can't find the node before current node, so we can't delete current node directly.
        node.next = node.next.next  #But we can let the value of current node be the value of next node and delete next node.
                                    #It's like swap current node and next node.
