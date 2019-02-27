# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plus(self, head):                                           #Use recursion to perform plus one on less significant digit and return carry to more significant digit.
        if head is None:                                            #If head is none, it reaches the end, return 1.
            return 1
        c = self.plus(head.next)
        head.val, c = (head.val + c) % 10, (head.val + c) // 10     #Calculate result and carry in this digit.
        return c                                                    #Return result.
        
    def plusOne(self, head: ListNode) -> ListNode:
        c = self.plus(head)                                         #Plus one recursively.
        if c == 1:                                                  #Handle the carry on most significant digit and create a new head.
            newHead = ListNode(1)
            newHead.next = head
            head = newHead
        return head
