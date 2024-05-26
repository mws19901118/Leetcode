# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int, int):                                                                                                                                                  #Traverse substree to find the longest consecutive path in subtree, longest increasing consecutive path ending at root and longest decreasing consecutive path ending at root.
            if not root:                                                                                                                                                                                            #If root is none, return 0, 0, 0.
                return 0, 0, 0
            leftMax, leftIncreaseMax, leftDecreaseMax = traverse(root.left)                                                                                                                                         #Traverse left subtree.
            rightMax, rightIncreaseMax, rightDecreaseMax = traverse(root.right)                                                                                                                                     #Traverse right subtree.
            currentIncreaseMax = max(leftIncreaseMax * int(root.left != None and root.val - root.left.val == 1), rightIncreaseMax * int(root.right != None and root.val - root.right.val == 1)) + 1                 #Calculate current longest increasing consecutive path ending at root.
            currentDecreaseMax = max(leftDecreaseMax * int(root.left != None and root.val - root.left.val == -1), rightDecreaseMax * int(root.right != None and root.val - root.right.val == -1)) + 1               #Calculate current longest decreasing consecutive path ending at root.
            leftToRightIncreaseMax = (leftIncreaseMax + rightDecreaseMax + 1) if root.left and root.right and root.val - root.left.val == 1 and root.val - root.right.val == -1 else 0                              #Calculate longest increasing consecutive path from left passing root towards right, if any.
            leftToRightDecreaseMax = (leftDecreaseMax + rightIncreaseMax + 1) if root.left and root.right and root.val - root.left.val == -1 and root.val - root.right.val == 1 else 0                              #Calculate longest decreasing consecutive path from left passing root towards right, if any.
            return max(leftMax, rightMax, currentIncreaseMax, currentDecreaseMax, leftToRightIncreaseMax, leftToRightDecreaseMax), currentIncreaseMax, currentDecreaseMax                                           #Current longest consecutive path is the max among leftMax, rightMax, currentIncreaseMax, currentDecreaseMax, leftToRightIncreaseMax, leftToRightDecreaseMax; also return currentIncreaseMax and currentDecreaseMax.
        return traverse(root)[0]
