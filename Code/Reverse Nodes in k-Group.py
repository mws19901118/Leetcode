# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if  head==None:                               #If the linked list is empty, return none.
            return None
        count=0
        nextgroup=head
        while nextgroup!=None and count<k:            #Find the (k+1)-th element in the linked list.
            nextgroup=nextgroup.next
            count+=1
        if count<k:                                   #If the number of elements in the linked list is smaller than k, return the head node.
            return head
        tail=head
        cursor=head.next
        for i in range(k-1):                          #Otherwise, reverse the first k elements.
            currenthead=cursor
            cursor=cursor.next
            currenthead.next=head
            head=currenthead
        tail.next=self.reverseKGroup(nextgroup, k)    #Recursively reverse the remain linked list and append the result to the tail of reversed first part of linked list.
        return head
