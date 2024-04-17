# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = None                                                          #Initialize result.
        def dfs(root: Optional[TreeNode], suffix: str) -> None:                #DFS with the suffix from upper level.
            if not root:                                                       #If root is not none, directly return.
                return
            currentStr = chr(ord('a') + root.val) + suffix                     #Generate string from current node to root.
            if not root.left and not root.right:                               #If root is leaf node, we don't need to go further.
                nonlocal result
                if result is None or currentStr < result:                      #If result is none or currentStr is smaller than result, set result to currentStr.
                    result = currentStr
                return
            dfs(root.left, currentStr)                                         #DFS left subtree with currentStr as suffix.
            dfs(root.right, currentStr)                                        #DFS right subtree with currentStr as suffix.
        
        dfs(root, "")                                                          #Start DFS from root with empty suffix.
        return result
