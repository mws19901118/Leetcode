# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, currentMax: int) -> int:
        if not root:                                          #If root is none, return 0.
            return 0
        count = 1 if currentMax <= root.val else 0            #If currentMax <= root.val, count = 1; otherwise count = 0.
        currentMax = max(currentMax, root.val)                #Update currentMax.
        count += self.dfs(root.left, currentMax)              #DFS left child and add result to count.
        count += self.dfs(root.right, currentMax)             #DFS right child and add result to count.
        return count
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -10001)                         #Starting DFS with a really small value.
