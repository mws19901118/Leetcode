# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummyHead = PolyNode()                                                                                #Initialize dummy head.
        tail = dummyHead                                                                                      #Initialize tail.
        while poly1 and poly2:                                                                                #Iterate while both poly1 and poly2 are not none.
            if poly1.power > poly2.power:                                                                     #If poly1 has higher power, append it to tail and move poly1 to next.
                tail.next = poly1
                tail = tail.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:                                                                   #If poly2 has higher power, append it to tail and move poly2 to next.
                tail.next = poly2
                tail = tail.next
                poly2 = poly2.next
            else:                                                                                             #Otherwise, we need calculation.
                if poly1.coefficient + poly2.coefficient:                                                     #If sum of 2 coefficients are not 0, append a new node with sumed coefficient and same power to tail.
                    tail.next = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power, None)
                    tail = tail.next
                poly1, poly2 = poly1.next, poly2.next                                                         #Move forward both poly1 and poly2.
        tail.next = poly1 if poly1 else poly2                                                                 #Append the remain of poly1 or poly2 to tail.
        return dummyHead.next                                                                                 #Return the next of dummy head.
