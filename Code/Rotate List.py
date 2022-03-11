# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        count = 1
        tail = head
        while tail.next is not None:                    #Calculate the length of list.
            tail = tail.next
            count += 1
        for i in range(count - k % count):              #K might be greater than length. Shift head to tail for count - k % count times.
            tail.next = head
            head = head.next
            tail.next.next = None
            tail = tail.next
        return head
