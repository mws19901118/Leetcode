# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        count = 0
        curr = head
        while curr:                             #Count linked list length.
            count += 1
            curr = curr.next
        a, b = None, None                       #Initialize the 2 nodes to swap with None.
        curr = head
        step = 0
        while not a or not b:                   #Traverse linked list until both a and b are set.
            step += 1
            if step == k:                       #If step equals k, point a to current node.
                a = curr
            if step == count - k + 1:           #If step equals count - k + 1, point b to current node.
                b = curr
            curr = curr.next
        a.val, b.val = b.val, a.val             #Swap a.val and b.val.
        return head                             #Return head.
