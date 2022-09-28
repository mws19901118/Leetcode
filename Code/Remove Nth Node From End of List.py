# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1, head)              #Create a dummy head.
        fast, slow = dummyHead, dummyHead           #Initialize fast and slow pointers.
        for _ in range(n):                          #Move fast n nodes ahead of slow.
            fast = fast.next
        while fast.next:                            #Move fast and slow forward until fast reaches the end of linked list.
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next                  #Remove the next node of slow.
        return dummyHead.next                       #Return the next node of dummy head.
