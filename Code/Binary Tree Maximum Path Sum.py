# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int):                                                        #Traverse subtree to return the max path sum in subtree and max path sum from root.
            if not root:                                                                                             #If root is none, return -inf and -inf.
                return -inf, -inf
            leftMax, leftRootMax = traverse(root.left)                                                               #Traverse left subtree.
            rightMax, rightRootMax = traverse(root.right)                                                            #Traverse right subtree.
            currRootMax = max(leftRootMax, rightRootMax, 0) + root.val                                               #Calculate current max path sum from root.
            return max(leftMax, rightMax, currRootMax, leftRootMax + rightRootMax + root.val), currRootMax           #Return new max path sum and current max path sum from root.
        return traverse(root)[0]                                                                                     #Return the max path sum of of traversing starting from root.
