# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while head!=None and head.val==val:   #Deal with the situation that value of head equals val.
            head=head.next
        if head==None:                        #If head is none, return none.
            return None
        cursor=head
        while cursor.next!=None:
            if cursor.next.val!=val:
                cursor=cursor.next
            else:
                cursor.next=cursor.next.next  #If value of the next node of cursor equals val, delete it.
        return head
