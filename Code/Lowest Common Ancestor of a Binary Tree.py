# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:                      #If root is none or root is p or q, return itself.
            return root
        left = self.lowestCommonAncestor(root.left, p, q)           #Get the LCA of p and q in the tree whose root is the left child of current root.
        right = self.lowestCommonAncestor(root.right, p, q)         #Get the LCA of p and q in the tree whose root is the right child of current root.
        if left and right:                                          #If root is not the LCA of p and q, either p or q must be none.
            return root
        else:
            return left if left else right
