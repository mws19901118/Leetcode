# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):        #The idea is merge sort.
        newlist=ListNode(-1)                #Use a fake head for convenience.
        tail=newlist
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tail.next=l1
                tail=tail.next
                l1=l1.next
            else:
                tail.next=l2
                tail=tail.next
                l2=l2.next
        if l1==None:
            tail.next=l2
        else:
            tail.next=l1
        newlist=newlist.next
        return newlist
