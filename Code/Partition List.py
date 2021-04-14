# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        firstHalfHead, secondHalfHead = ListNode(), ListNode()              #Initialize the dummy head of first half and second half.
        firstHalfTail, secondHalfTail = firstHalfHead, secondHalfHead       #Initialize the tail of first half and second half.
        while head:                                                         #Traverse list.
            if head.val < x:                                                #Append to first half if current node value is smaller than x.
                firstHalfTail.next = head
                firstHalfTail = firstHalfTail.next
            else:                                                           #Otherwise append to second half.
                secondHalfTail.next = head
                secondHalfTail = secondHalfTail.next
            head = head.next                                                #Move to next.
            firstHalfTail.next, secondHalfTail.next = None, None            #Reset the next of both tail.
        firstHalfTail.next = secondHalfHead.next                            #Point first half tail to the next of second half head.
        return firstHalfHead.next                                           #Return the next of first half head.
