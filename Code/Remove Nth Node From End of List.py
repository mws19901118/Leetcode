# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        fast=head
        slow=head
        for i in range(n):
            fast=fast.next              #Let fast pointer be exactly n nodes after slow pointer.
        if fast==None:                  #If fast is none, i.e. we have to remove the first node, return the next node of head.
            return head.next
        while fast.next!=None:          #Move fast pointer and slow pointer afterward synchronously, until fast is the tail of the linked list.
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next        #Then the next node of slow is the n-th node form end, so remove it.
        return head
