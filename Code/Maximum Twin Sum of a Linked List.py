# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head                             #Use fast and slow pointers to find the mid point of linked list.
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = fast.next
        curr = slow.next                                    #Reverse the second half.
        while curr is not fast:
            slow.next = curr.next
            curr.next = fast.next
            fast.next = curr
            curr = slow.next
        result = 0                                          #Find the max twin sum by traversing first half and second half simultaneously.
        while curr:
            result = max(head.val + curr.val, result)
            head = head.next
            curr = curr.next
        return result
