# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:                                                                                                                    #If root is none, return 0.
            return 0
        result = root.left.val if root.left and not root.left.left and not root.left.right else self.sumOfLeftLeaves(root.left)         #If the left child of root is left leave, initialize result to be the value of left child; otherwise, initialize result to be the recursion result of left child.
        return result + self.sumOfLeftLeaves(root.right)                                                                                #Return result plus the recursion result of right child.
