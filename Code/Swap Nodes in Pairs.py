# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):                #A special case of Reverse Nodes in k-Group for k=2.
        if  head==None:
            return None
        if head.next==None: 
            return head
        nextpair=head.next.next               #Find the beginning of remaining linked list leaving out the first pair.
        newhead=head.next                     #Reverse the first pair.
        newhead.next=head
        head.next=self.swapPairs(nextpair)    #Reverse the remaining linked list recursively and append the result to the tail of reversed first pair.
        return newhead
