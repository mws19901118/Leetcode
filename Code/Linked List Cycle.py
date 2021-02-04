# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:                                    #If head is none, return none.
            return False
        fast, slow = head, head
        while fast.next and fast.next.next:             #Fast and slow pointers.
            fast = fast.next.next
            slow = slow.next
            if fast == slow:                            #If fast meets slow, return true.
                return True
        return False                                    #Return false.
