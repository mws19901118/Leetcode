# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pointerA, pointerB = headA, headB                                   #Have a pointer starting at headA and a pointer starting at headB.
                                                                            #Suppose linked list A can be divided to a + c while linked list B can be divided to b + c and a is the exclusive part of A, b is the exclusive part of B and c is the common tail after intersection.
        while pointerA != pointerB:                                         #While they are not equal, keep traversing. Pointer A will traverse a, c, b in order while pointer B will traverse b, c, a in order. Finally they will meet at the start of c.
            pointerA = headB if pointerA is None else pointerA.next         #If pointer A is none, pointer A has traversed a + c, reset it to headB to traverse b; otherwise, move to its next.
            pointerB = headA if pointerB is None else pointerB.next         #If pointer B is none, pointer B has traversed b + c, reset it to headA to traverse a; otherwise, move to its next.
        return pointerA                                                     #Return pointer A: if there is intersection, pointer A is the intersection; if not, pointer A is none.
