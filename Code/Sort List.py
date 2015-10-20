# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self,left,right):                         #merge
        nullhead=ListNode(0)
        tail=nullhead
        while left!=None and right!=None:  
            if left.val<=right.val:
                tail.next=left
                left=left.next
            else:  
                tail.next=right
                right=right.next
            tail=tail.next
        if left==None:
            tail.next=right
        if right==None:
            tail.next=left
        return nullhead.next  
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head; fast = head                        #fast pointer and slow pointer, in order to cut off the list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None                                #head1 and head2 are the head of two new list, respectively
        head1 = self.sortList(head1)                    #sort head1
        head2 = self.sortList(head2)                    #sort head2
        head = self.merge(head1, head2)                 #merge
        return head
