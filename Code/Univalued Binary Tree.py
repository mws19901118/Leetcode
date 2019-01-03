# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            return self.isUnivalTree(root.right) and root.val == root.right.val
        elif root.right is None:
            return self.isUnivalTree(root.left) and root.val == root.left.val
        else:
            return self.isUnivalTree(root.right) and root.val == root.right.val and self.isUnivalTree(root.left) and root.val == root.left.val
