# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:                                                                                             #If p and q are both empty, they are same.
            return True
        elif (p and not q) or (not p and q) or p.val != q.val:                                                          #If one is empty but the other is not or the values don't match, they are not same.
            return False
        else:                                                                                                           #If the left child of p and the left child of q are same, and the right child of p and right child of q are same, the value of p is equal to the value of q, they are same.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
