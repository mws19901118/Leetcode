# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root:                                                              #If root is none, directly return root.
            root.left = self.pruneTree(root.left)                             #Prune left subtree.
            root.right = self.pruneTree(root.right)                           #Prune right subtree.
            if root.val == 0 and (not root.left) and (not root.right):        #If root val is 0 and both left subtree and right subtree is none or has been pruned, set root to none to prune it.
                root = None
        return root
