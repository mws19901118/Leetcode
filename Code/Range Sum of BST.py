# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return 0 if not root else self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (root.val if root.val >= low and root.val <= high else 0)  #If root is none, return 0. Otherwise, calculate the range sum in left child and right child. If the value of root is in range, add it to sum.
