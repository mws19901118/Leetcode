# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head==None:
            return None
        pre=ListNode(-1)                                      #Record the node before where we insert node.
        cursor=head
        if head.val>=x:                                       #If we have to insert before the head node, add a fake head.
            fakehead=ListNode(-1)
            fakehead.next=head
            pre=fakehead
        else:
            while cursor.next!=None and cursor.next.val<x
                cursor=cursor.next
            pre=cursor
        split=pre.next                                        #This is the first node whose value is larger than or equal to x. Whenever we insert a node before it, the next of inserted node should point to it.
        while cursor.next!=None:
            if cursor.next.val<x:                             #Find the value to insert before split.
                pre.next=cursor.next
                if cursor.next.next!=None:
                    temp=cursor.next.next
                else:                                         #If it is the tail of the linked list, the next of cursor is none.
                    temp=None
                pre=pre.next
                pre.next=split
                cursor.next=temp
            else:
                cursor=cursor.next
        if head.val>=x:                                       #If the split node is head, return the next of fake head; otherwise, return head.
            return fakehead.next
        else:
            return head
