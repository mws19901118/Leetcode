# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache                                                                    #Cache result.
        def dp(start: int, end: int) -> List[Optional[TreeNode]]:                 #DP to find all unique BST formed by [start, end].
            if start > end:                                                       #If start > end, there is no valid BST, return [None].
                return [None]
            result = []                                                           #Initialize result.
            for i in range(start, end + 1):                                       #Enumerate root from start to end.
                left, right = dp(start, i - 1), dp(i + 1, end)                    #Find all unique BST for the left subtree and right subtree respectively.
                for x, y in product(left, right):                                 #Emunerate each pair of left subtree and rifght subtree.
                    result.append(TreeNode(i, x, y))                              #Append the BST to result.
            return result                                                         #Return result.

        return dp(1, n)                                                           #Return dp(1, n).
