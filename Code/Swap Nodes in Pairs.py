# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:                       #If less than 2 nodes in linked list, return head directly.
            return head
        tail = head.next                                    #Get the tail of first pair.
        head.next = self.swapPairs(tail.next)               #Reverse the remaining of linked list and set next of head to it.
        tail.next = head                                    #Set next ot tail to head
        return tail                                         #Return tail after the reverse.
