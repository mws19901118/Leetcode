# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int, int):                                                                                      #Traverse subtree to return minDiff, minValue and maxValue.
            if not root:                                                                                                                                #If root is none, return positive infinite, possitive infinite and negative infinite respectively.
                return (float('inf'), float('inf'), float('-inf'))
            leftMinDiff, leftMin, leftMax = traverse(root.left)                                                                                         #Traverse root.left.
            rightMinDiff, rightMin, rightMax = traverse(root.right)                                                                                     #Traverse root.right.
            return min(leftMinDiff, rightMinDiff, root.val - leftMax, rightMin - root.val), min(leftMin, root.val), max(rightMax, root.val)             #Return minDiff, minValue and maxValue for current subtree.
        return traverse(root)[0]    
