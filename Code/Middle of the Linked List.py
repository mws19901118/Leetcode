# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head       #Fast and slow pointers.
        while fast and fast.next:     #Fast pointer moves twice while slow pointer moves once.
            fast = fast.next.next     #When fast pointer reaches the end, slow pointer is in the middle.
            slow = slow.next
        return slow
