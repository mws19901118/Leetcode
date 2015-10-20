# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head==None or head.next==None:
            return True
            
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:   #Use fast pointer and slow pointer to find the mid node of linked list.
            fast=fast.next.next
            slow=slow.next
        if fast.next!=None:
            fast=fast.next
        slow=slow.next
        
        current=slow.next                                 #Reverse the second half of the linked list.
        slow.next=None
        while current!=None:
            temp=current
            current=current.next
            temp.next=slow
            slow=temp
            
        while slow!=None:                                 #Compare the value of each node of first half and reversed second half.
            if slow.val!=head.val:                        #If there are an unmatched pair of nodes, the linked list in not palindrome.
                return False
            else:
                slow=slow.next
                head=head.next
        return True
