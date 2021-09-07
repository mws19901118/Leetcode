# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(None)              #Create a dummy node.
        while head:                             #Travese linked list.
            curr = head                         #Get current node.
            head = head.next                    #Move head to next.
            curr.next = dummyHead.next          #Point next of current node to next of dummyHead.
            dummyHead.next = curr               #Insert curr after dummyHead.
        return dummyHead.next                   #Return the next of dummyHead.
