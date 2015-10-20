# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        fakehead=ListNode(-1)                                                   #Because head may be deleted, add a fakehead before the head node.
        fakehead.next=head
        current=fakehead                                                        #Record the current node whose link is to be determined.
        while current.next!=None:
            nextnode=current.next
            count=1
            while nextnode.next!=None and nextnode.next.val==current.next.val:
                count+=1                                                        #Count the number of appereance.
                nextnode=nextnode.next
            if count>1:
                current.next=nextnode.next                                      #Delete the duplicate nodes.
            else:
                current=current.next
        return fakehead.next
