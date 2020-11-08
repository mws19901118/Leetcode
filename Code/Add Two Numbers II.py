# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linkListToNumber(self, head: ListNode) -> int:                        #Convert linked list to int.
        number = 0
        while head:
            number = number * 10 + head.val
            head = head.next
        return number
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = self.linkListToNumber(l1) + self.linkListToNumber(l2)        #Sum up the value after converting l1 and l2 to int.
        dummyHead = ListNode()                                                #Create a dummy head.
        while True:                                                           #Covert sum to linked list.
            node = ListNode(number % 10, dummyHead.next)
            dummyHead.next = node
            number //= 10
            if number == 0:
                break
        return dummyHead.next
