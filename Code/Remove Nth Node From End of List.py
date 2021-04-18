# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):              #Let fast pointer be exactly n nodes after slow pointer.
            fast = fast.next
        if not fast:                    #If fast is none, i.e. we have to remove the first node, return the next node of head.
            return head.next
        while fast.next:                #Move fast pointer and slow pointer afterward synchronously, until fast is the tail of the linked list.
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next      #Then the next node of slow is the n-th node form end, so remove it.
        return head                     #Return head.
