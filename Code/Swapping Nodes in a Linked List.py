# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k - 1):                  #Find the k-th node from beginning.
            curr = curr.next
        a, b = curr, head                       #Store it in a and then create a new pointer from beginning.
        while curr.next:                        #Move curr and b both towards end; when curr is the end, b is the k-th node from the end.
            curr = curr.next
            b = b.next
        a.val, b.val = b.val, a.val             #Swap a.val and b.val.
        return head                             #Return head.
