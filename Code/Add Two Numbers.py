# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry=0
        head=l1                                     #Use l1 to store the result.
        junction=None
        while l1!=None and l2!=None:
            newval=(l1.val+l2.val+carry)%10         #Calculate the sum while neither of l1 nor l2 ends.
            carry=(l1.val+l2.val+carry)/10
            l1.val=newval
            if l1.next==None or l2.next==None:      #Use juction to record current l1 if the next node of l1 is none or the next node of l2 is none.
                junction=l1
            l1=l1.next
            l2=l2.next
        if l1==None:                                #To keep the value of sum, append the remain part to l2 to junction, if l1 is none.
            junction.next=l2
        l1=junction.next                            #Set l1 to be the next node of junction.
        while l1!=None and carry==1:                #While l1 doesn't end and carry is 1, continue calculating the sum.
            newval=(l1.val+carry)%10
            carry=(l1.val+carry)/10
            l1.val=newval
            if l1.next==None:                       #Use juction to record current l1 if the next node of l1 is none.
                junction=l1
            l1=l1.next
        if carry==1:                                #If carry is still 1, append a listnode with 1 to junction.
            junction.next=ListNode(1)
        return head
