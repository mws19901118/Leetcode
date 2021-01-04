# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()                                                  #Create a dummy head.
        tail = dummyHead
        while l1 and l2:                                                        #Compare l1 and l2 while there are both not none, then append the smaller one to tail and move l1 or l2.
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2                                            #Append the remaining(either l1 or l2) to tail.
        return dummyHead.next                                                   #Return the next of dummy head.
