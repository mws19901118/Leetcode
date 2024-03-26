# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummyHead = ListNode(0, list1)        #Create a dummy haed for list1.
        curr = dummyHead
        for _ in range(a):                    #Move a steps from dummy head.
            curr = curr.next
        removed = curr.next                   #Get the head of nodes to be removed.
        curr.next = list2                     #Insert list2 after the place it should be merged.
        while curr.next:                      #Go to the tail of list2.
            curr = curr.next
        for _ in range(b - a):                #Remove b - a nodes from removed.
            removed = removed.next
        curr.next = removed.next              #Append removed to the tail of list2.
        return dummyHead.next                 #Return the next of dummy head.
