# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyHead = ListNode(0, head)                                                       #Create a dummy head for current linked list.
        curr = dummyHead
        for i in range(left - 1):                                                           #Traverse linked list to find the node before the position left.
            curr = curr.next
        dummyHeadForReverse = ListNode()                                                    #Create a dummy head for reversed linked list.
        tail = curr.next                                                                    #Point the tail of reversed linked list to the node on position left.
        for i in range(right - left + 1):                                                   #Reverse from position left to position right.
            temp = curr.next                                                                #Temporarily store current node.
            curr.next = curr.next.next                                                      #Remove it from linked list.
            temp.next, dummyHeadForReverse.next = dummyHeadForReverse.next, temp            #Insert it after the dummy head of reversed linked list.
        tail.next = curr.next                                                               #Point next of tail to the node after position right.
        curr.next = dummyHeadForReverse.next                                                #Point the next of node before position left to the next of dummy node of reversed linked list.
        return dummyHead.next                                                               #Return the next of dummy head.
