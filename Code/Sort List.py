# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:                         #Merge 2 sorted linked list.
        dummyHead = ListNode(0)
        tail = dummyHead
        while left is not None and right is not None:  
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:  
                tail.next = right
                right = right.next
            tail = tail.next
        if left is None:
            tail.next = right
        if right is None:
            tail.next = left
        return dummyHead.next  
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        slow, fast = head, head                                                         #fast pointer and slow pointer, in order to cut off the list.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None                                                                #head1 and head2 are the head of two new list, respectively.
        head1 = self.sortList(head1)                                                    #Sort head1.
        head2 = self.sortList(head2)                                                    #Sort head2.
        head = self.merge(head1, head2)                                                 #Merge.
        return head        
