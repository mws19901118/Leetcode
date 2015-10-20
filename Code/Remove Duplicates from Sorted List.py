# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current=head                                                  #Record current node.
        while current!=None:
            nextnode=current.next
            while nextnode!=None and nextnode.val==current.val:       #Find the next node whose value is not equal to current node's value.
                nextnode=nextnode.next
            current.next=nextnode                                     #Link current node to next node.
            current=current.next
        return head
