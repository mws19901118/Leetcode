# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:                                                                                            #If head is none, return none.
            return None
        if not head.next:                                                                                       #If head only has one node, instantiate a tree node for it and return.
            return TreeNode(head.val, None, None)
        fast, slow = head, head                                                                                 #Use fast and slow pointers to find the mid of linked list.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = head                                                                                             #Find the tail of first half and cut its link with slow.
        while tail.next != slow:
            tail = tail.next
        tail.next = None
        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))                  #Construct the left subtree and right subtree from fitst hald and second half respectively in recursion, then instantiate root node and return.
