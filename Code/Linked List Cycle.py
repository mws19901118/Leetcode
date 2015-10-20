# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head==None:
            return False
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:           #fast pointer and slow pointer
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
