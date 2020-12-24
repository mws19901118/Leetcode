# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if  head is None:
            return None
        if head.next is None: 
            return head
        head.next.next = self.swapPairs(head.next.next)     #Reverse the linked list after first pair. 
        tail = head.next
        head.next = tail.next                               #Set the next of head to be next of tail.
        tail.next = head                                    #Reverse first pair.
        return tail                                         #Return the new head.
