# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast.next and fast.next.next:                             #Use fast pointer and slow pointer to find the mid node of linked list.
            fast = fast.next.next
            slow = slow.next
        dummy = ListNode()
        curr = slow.next
        while curr:                                                     #Reverse the second half of the linked list.
            temp = curr
            curr = curr.next
            temp.next = dummy.next
            dummy.next = temp
        a, b = head, dummy.next
        while a and b and a.val == b.val:                               #Compare the value of each node of first half and reversed second half.
            a, b = a.next, b.next
        return b is None                                                #If there are an unmatched pair of nodes, the linked list in not palindrome.
