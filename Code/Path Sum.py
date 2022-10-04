# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:                                                                                                        #If root is none, return false.
            return False
        if not root.left and not root.right:                                                                                #If root is leaf node, return wether its value equals targetSum.
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)        #Traverse in both sub tree; if either is true, then return true.
