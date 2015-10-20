# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head==None:
            return head
        current=head.next                       #Record current node.
        head.next=None                          #After reverse, the original head node will become tail, so set the next node of head to none.
        while current!=None:
            nextnode=current.next               #Record the next node of current node.
            current.next=head                   #Insert current node in front of head node.
            head=current                        #Update head node.
            current=nextnode                    #Update current node.
        return head
