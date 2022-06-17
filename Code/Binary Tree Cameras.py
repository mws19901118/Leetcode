# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode) -> Tuple:                 #DFS, return a tuple of min cameras needed in 3 situations(all nodes covered except node, all nodes covered and no camera placed at node, all nodes covered and camera placed at node).
        if not node:                                        #If node is none, return (0, 0, inf).
            return 0, 0, float('inf')
        l, r = self.dfs(node.left), self.dfs(node.right)    #DFS left subtree and right subtree.
        dp0 = l[1] + r[1]                                   #To cover all nodes except node, left subtree and right subtree have to be covered but camera cannot be placed at left child or right child.
        dp1 = min(l[2] + min(r[1:]), r[2] + min(l[1:]))     #To cover all nodes and not place camera at node, camera needs to be placed at left child or right child.
        dp2 = 1 + min(l) + min(r)                           #To cover all nodes and place camera at node, the left child and right child are automatically covered. 
        return dp0, dp1, dp2
    
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return min(self.dfs(root)[1:])                      #DFS from root and return the min value of cameras needed to cover all nodes, either place camera at root or not.
