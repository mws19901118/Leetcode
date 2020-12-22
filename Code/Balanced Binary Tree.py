# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: TreeNode) -> int:
        if root is None:                                                                                                                            #If root is none, return 0.
            return 0
        leftHeight, rightHeight = self.height(root.left), self.height(root.right)                                                                   #Get the height of left subtree and right subtree.
        return max(leftHeight, rightHeight) + 1 if leftHeight != -1 and rightHeight != -1 and abs(leftHeight - rightHeight) <= 1 else -1            #If both left subtree and right subtree is balanced and the height difference is no more than 1, return the depth of current tree; otherwise return -1.
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1
