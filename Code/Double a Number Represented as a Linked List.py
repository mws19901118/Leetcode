# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def innerDouble(head: Optional[ListNode]) -> int:                #Double digit and return carry.
            if not head:                                                 #If head is none, return 0.
                return 0
            carry = innerDouble(head.next)                               #Recursively double the next of current node and get the carry.
            newCarry, head.val = divmod(head.val * 2 + carry, 10)        #Calculate the carry and update value.
            return newCarry                                              #Return new carry.

        carry = innerDouble(head)                                        #Double existing linked list.
        return ListNode(carry, head) if carry else head                  #If there is a carry, create a new node as head with carry value and return; otherwise just return head.
