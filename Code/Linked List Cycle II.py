# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head==None:
            return None
        fast=head
        slow=head
        cyclenode=None
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:                                #judge whether the list has cycle
                cyclenode=slow
                break
        if cyclenode==None:
            return None
        else:
            newhead=cyclenode.next                        #cut the list into a 'Y' shape one and the 'Y' node is the node where the cycle begins
            cyclenode.next=None
            len1=0                                        #count the distance between 'Y' node and bifurcation 1
            temp1=head
            while temp1!=cyclenode:
                len1+=1
                temp1=temp1.next
            len2=0
            temp2=newhead                                 #count the distance between 'Y' node and bifurcation 2
            while temp2!=cyclenode:
                len2+=1
                temp2=temp2.next
            temp1=head
            temp2=newhead
            if len1>=len2:                                #the longer bifurcation move forword |len1-len2| times
                t=len1-len2
                while t!=0:
                    temp1=temp1.next
                    t-=1
            else:
                t=len2-len1
                while t!=0:
                    temp2=temp2.next
                    t-=1
            while temp1!=temp2:                           #the 'Y' node is the first node where temp1=temp2
                temp1=temp1.next
                temp2=temp2.next
            return temp1
