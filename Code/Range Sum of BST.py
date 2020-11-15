# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:                                                                              #If root is none, return 0.
            return 0
        s = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)          #Calculate the range sum in left child and right child.
        s += root.val if root.val >= low and root.val <= high else 0                                  #If the value of root is in range, add it to sum.
        return s
