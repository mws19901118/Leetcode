# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head==None:
            return None
        length=1
        tail=head
        while tail.next!=None:
            tail=tail.next
            length+=1                                             #Calculate the length of list.
        for i in range(length-k%length):                          #K might be greater than length.
            tail.next=head
            head=head.next
            tail.next.next=None
            tail=tail.next
        return head
