# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head                                                          #Initialize a pointer.
        while curr.next:                                                     #While curr.next is not none, insert gcd.
            curr.next = ListNode(gcd(curr.val, curr.next.val), curr.next)    #Insert gcd of curr.val and curr.next.val after curr.
            curr = curr.next.next                                            #Move curr to curr.next.next.
        return head
