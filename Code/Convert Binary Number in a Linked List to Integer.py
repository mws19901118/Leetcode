# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        while head:                                   #Traverse through the linked list.
            decimal = (decimal << 1) | head.val       #Shift decimal 1 bit left and OR with value of current linked list node.
            head = head.next
        return decimal
