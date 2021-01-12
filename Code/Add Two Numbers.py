# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode()                      #Create a dummy head for result.
        tail = dummyHead
        carry = 0                                   #Initialize carry to be 0.
        while l1 and l2:                            #While both l1 and l2 is not none, calculate sum and append to tail.
            x = l1.val + l2.val + carry
            carry = x // 10                         #Update carry.
            tail.next = ListNode(x % 10)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        remain = l1 if l1 else l2                   #Check if there is l1 or l2 remaining.
        while remain:                               #While remain is not none, calculate sum and append to tail.
            x = remain.val + carry
            carry = x // 10                         #Update carry.
            tail.next = ListNode(x % 10)
            tail = tail.next
            remain = remain.next
        if carry:                                   #If carry is 1, append it to tail.
            tail.next = ListNode(carry)
        return dummyHead.next                       #Return the next of dummy head.
        
