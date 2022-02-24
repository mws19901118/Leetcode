# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:                               #If head is none or only has one node, directly return head.
            return head
        fast, slow = head, head                                     #Use fast & slow pointers to find the mid point of list.
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None                                            #Cut list into 2 halves.
        h1, h2 = self.sortList(head), self.sortList(h2)             #Sort first half and second half respectively.
        dummyHead = ListNode()                                      #Initialize a dummy head.
        tail = dummyHead
        while h1 and h2:                                            #Merge first half and second half.
            if h1.val <= h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        tail.next = h1 if h1 else h2
        return dummyHead.next                                       #Return the next of dummy head.
