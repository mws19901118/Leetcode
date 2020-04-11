# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root: TreeNode) -> tuple:                                            #For each node, find the height of node plus one and the diameter of the subtree.
        if root is None:
            return (0, 0)
        left = self.traverse(root.left)                                                     #Traverse through left subtree.
        right = self.traverse(root.right)                                                   #Traverse through right subtree.
        return (max(left[0], right[0]) + 1, max(left[1], right[1], left[0] + right[0]))     #Calculete the height and diameter. Diameter should be the max of left subtree diameter, right subtree diameter and the sum of left child height plus one and right child hight plus one.
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.traverse(root)[1]                                                       #Return the diameter.
