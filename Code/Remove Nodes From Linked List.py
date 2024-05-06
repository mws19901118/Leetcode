# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:                        #Reverse linked list.
            dummyHead = ListNode()
            while node:
                curr = node
                node = node.next
                curr.next = dummyHead.next
                dummyHead.next = curr
            return dummyHead.next
        
        reversedList = reverse(head)                                    #Reverse given linked list.
        maxValue = -1                                                   #Initialize max value from right.
        dummyHead = ListNode()                                          #Instantiate a dummy head.
        tail = dummyHead
        while reversedList:                                             #Traverse reversed linked list.
            if reversedList.val < maxValue:                             #If current node value is smaller than max value, it has a node with greater value to the right side, so skip it.
                reversedList = reversedList.next
            else:                                                       #Otherwise, we should keep current node.
                tail.next = reversedList                                #Append it to the tail of new linked list.
                maxValue = max(maxValue, reversedList.val)              #Update max value.
                reversedList = reversedList.next                        #Move to next.
                tail = tail.next
                tail.next = None
        return reverse(dummyHead.next)                                  #Reverse the new linked list again and return.
