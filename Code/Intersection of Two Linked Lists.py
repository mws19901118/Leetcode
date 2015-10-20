# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None:
            return None
        if headB==None:
            return None
        lengthA=1
        lengthB=1
        tempA=headA
        tempB=headB
        while tempA.next!=None:
            tempA=tempA.next
            lengthA+=1
        while tempB.next!=None:
            tempB=tempB.next
            lengthB+=1
        if tempA!=tempB:                                      //Judge if the 2 linked list intersect.
            return None
        else:
            tempA=headA
            tempB=headB
            if lengthA>lengthB:
                for i in range(0,lengthA-lengthB):
                    tempA=tempA.next
            else:
                for i in range(0,lengthB-lengthA):
                    tempB=tempB.next
            while tempA!=tempB:
                tempA=tempA.next
                tempB=tempB.next
            return tempA
