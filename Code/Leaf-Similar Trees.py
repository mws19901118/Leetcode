# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preOrderTraverse(root, leafValues):           #Store leaf values in sequence in an array by pre-order traversal recursively.
    if root is None:
        return
    if root.left is None and root.right is None:
        leafValues.append(root.val)
        return
    preOrderTraverse(root.left, leafValues)
    preOrderTraverse(root.right, leafValues)

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafValues1 = []
        leafValues2 = []
        preOrderTraverse(root1, leafValues1)      #Find the leaf values of root1.
        preOrderTraverse(root2, leafValues2)      #Find the leaf values of root2.
        return leafValues1 == leafValues2         #Compare.
