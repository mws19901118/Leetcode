# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummyHead = ListNode(None, head)                        #Create a dummy head.
        cursor = dummyHead
        while cursor and cursor.next:
            while cursor.next and cursor.next.val == val:       #If value of the next node of cursor equals val, delete it.
                cursor.next = cursor.next.next
            cursor = cursor.next
        return dummyHead.next
