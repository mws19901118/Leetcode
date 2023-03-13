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
        count, curr = 0, head                                                                                   #Count number of nodes.
        while curr:
            count += 1
            curr = curr.next
        tail = head
        for _ in range(count // 2 - 1):
            tail = tail.next
        mid = tail.next                                                                                         #Find mid point.
        tail.next = None                                                                                        #Cut before mid.
        return TreeNode(slow.val, self.sortedListToBST(head), self.sortedListToBST(slow.next))                  #Construct the left subtree and right subtree from fitst hald and second half respectively in recursion, then instantiate root node and return.
