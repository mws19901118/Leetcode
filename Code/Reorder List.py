# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head!=None and head.next!=None and head.next.next!=None:
            mid=head
            tail=head
            while tail.next!=None and tail.next.next!=None:
                tail=tail.next.next
                mid=mid.next
            if tail.next!=None:
                tail=tail.next
            newhead=mid.next                                #cut off the list
            mid.next=None
            count=1
            while newhead!=tail:                            #delete nodes of the second half of list successively, and insert them after tail to reverse the sequence
                temp=newhead
                newhead=newhead.next
                temp.next=tail.next
                tail.next=temp
                count+=1                                    #count the number of nodes of the second half of list
            cursor=head
            while count!=0:                                 #merge
                temp=newhead
                newhead=newhead.next
                temp.next=cursor.next
                cursor.next=temp
                cursor=cursor.next.next
                count-=1
