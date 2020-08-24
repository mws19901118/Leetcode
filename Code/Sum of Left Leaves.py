# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:                                            #If root is none, return 0.
            return 0
        result = self.sumOfLeftLeaves(root.right)               #Get the sum of left leaves in right subtree.
        if root.left:
            if root.left.left or root.left.right:               #If has left child and left child is not leave, get the sum of left leaves in left subtree.
                result += self.sumOfLeftLeaves(root.left)
            else:                                               #If has left child and left child is leave, add the value of left child to result.
                result += root.left.val
        return result
