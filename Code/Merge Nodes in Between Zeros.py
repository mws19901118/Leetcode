# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()                        #Create a dummy head for the result linked list.
        tail = dummyHead                              #Create a tail pointer.
        curr = head
        while curr.next:                              #Traverse current linked list.
            nodeSum = 0                               #Initialize sum.
            while curr.next.val != 0:                 #While the value of next node is not 0, add it to nodeSum and remove next node.
                nodeSum += curr.next.val
                curr.next = curr.next.next
            tail.next = ListNode(nodeSum, None)       #Append the sum node to tail.
            tail = tail.next                          #Move forward tail.
            curr.next = curr.next.next                #Remove next node as it is 0.
        return dummyHead.next                         #Return the next of dummy head.
