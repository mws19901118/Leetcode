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
        if (root.val <= p.val and root.val >= q.val) or (root.val <= q.val and root.val >= p.val):      #If root.val is between p.val and q.val, root is the LCA.
            return root
        elif root.val > p.val and root.val > q.val:                                                     #If root.val is greater than both p.val and q.val, the LCA is in the left child of root.
            return self.lowestCommonAncestor(root.left, p, q)
        else:                                                                                           #If root.val is smaller than both p.val and q.val, the LCA is in the right child of root.
            return self.lowestCommonAncestor(root.right, p, q)
