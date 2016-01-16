# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddhead = ListNode(-1)                      #Use a new linked list to store the odd nodes.
        evenhead = ListNode(-1)                     #Use a new linked list to store the even nodes.
        oddcurrent = oddhead
        evencurrent = evenhead
        isOdd = True                                #Indicate current node is odd or not.
        while head != None:
            if isOdd:                               #If current node is odd, append it to the odd linked list.
                oddcurrent.next = head
                oddcurrent = oddcurrent.next
                head = head.next
                oddcurrent.next = None
                isOdd = not isOdd                   #The next node is even.
            else:                                   #Otherwise, append it to the even linked list.
                evencurrent.next = head
                evencurrent = evencurrent.next
                head = head.next
                evencurrent.next = None
                isOdd = not isOdd                   #The next node is odd.
        oddcurrent.next = evenhead.next             #Link the actual head of even linked list and the tail of odd linked list.
        evenhead.next = None
        return oddhead.next                         #Return the actual head of odd linked list.
