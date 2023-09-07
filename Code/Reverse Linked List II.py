# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)            #Append a dummy head before the beginning of haed.
        rightTail = dummyHead                    #Find the right tail, which is the last node in reverse range.
        for _ in range(right):
            rightTail = rightTail.next
        leftTail = dummyHead                     #Find the left tail, which is the node before the first node in reverse range.
        for _ in range(left - 1):
            leftTail = leftTail.next
        for _ in range(left, right):             #Iterate right - left times.
            t = leftTail.next                    #Detach the node afte left tail from linked list.
            leftTail.next = t.next
            t.next = rightTail.next              #Attach the node after right tail.
            rightTail.next = t
        return dummyHead.next                    #Return the next of dummy head.
