# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head                     #Initialize fast and slow pointers.
        while fast.next and fast.next.next:         #Move fast 2 times and slow 1 time simultaneously towards end.
            fast = fast.next.next
            slow = slow.next
        dummyHead = ListNode()                      #Initialize a dummy head for second half.
        curr = slow.next                            #Next of slow is the start of second half.
        slow.next = None                            #Cut off between first half and second half.
        while curr:                                 #Reverse second half.
            temp = curr.next
            curr.next = dummyHead.next
            dummyHead.next = curr
            curr = temp
        shalf = dummyHead.next
        curr = head
        while shalf:                                #Insert reversed second half into first half.
            temp = shalf.next
            shalf.next = curr.next
            curr.next = shalf
            curr = curr.next.next
            shalf = temp
