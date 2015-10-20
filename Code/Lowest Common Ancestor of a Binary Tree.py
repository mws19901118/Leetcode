# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root==None or root==p or root==q:                  #If root is none or root is p or q, return itself.
            return root
        left=self.lowestCommonAncestor(root.left, p, q)       #Get the LCA of p and q in the tree whose root is the left child of current root.
        right=self.lowestCommonAncestor(root.right, p, q)     #Get the LCA of p and q in the tree whose root is the right child of current root.
        if left!=None and right!=None:                        #If root is not the LCA of p and q, either p or q must be none.
            return root
        elif left!=None:
            return left
        else:
            return right
