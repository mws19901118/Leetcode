# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def dp(self, root: TreeNode):                                                                   #Return the tuple of max money robbing current node and not robbing current node.
        if not root:                                                                                #If root is none, return (0, 0).
            return (0, 0)
        leftResult, rightResult = self.dp(root.left), self.dp(root.right)                           #Get the DP result from left child and right child.
        return (leftResult[1] + rightResult[1] + root.val, max(leftResult) + max(rightResult))      #If rob current node, the max money is the sum of not robbing both child plus current value; if not rob currentnode, the max money is the sum of max money of both child.
    
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))                                                                   #Return the DP result from root.
