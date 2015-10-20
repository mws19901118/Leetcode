# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        pre=head                                            #Record the node before the start node.
        if m==1:                                            #If the start node is head, add a fake head before head.
            fakehead=ListNode(-1)
            fakehead.next=head
            pre=fakehead
        else:
            for i in range(1,m-1):
                pre=pre.next
        cursor=pre.next                                     #Record the start node. Use it to pass through the linked list.
        for i in range(n-m):
            temp=cursor.next                                #Record the next node of cursor. Its next node should be linked by cursor.
            if temp.next!=None:                             
                cursor.next=temp.next
            else:                                           #If it is the tail of the linked list, the next of cursor is none.
                cursor.next=None
            temp.next=pre.next                              #After that, link temp to the next node of pre.
            pre.next=temp                                   #Then, link pre to temp.
        if m==1:                                            #If the start node is head, return the next of fake head; otherwise, return head.
            return fakehead.next
        else:
            return head
