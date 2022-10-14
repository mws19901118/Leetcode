# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)             #Initialize a dummy head.
        fast, slow = dummyHead, dummyHead         #Initialize fast and slow pointers.
        while fast.next and fast.next.next:       #Move fast pointer 2 steps a time while move slow pointer 1 step a time.
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next                #Remove the next of slow pointer.
        return dummyHead.next                     #Return the next of dummy head.
