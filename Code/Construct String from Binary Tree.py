# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:                                                #If root is none, return "".
            return ""
        result = str(root.val)                                      #Construct result to be root.val.
        if not root.left and not root.right:                        #If root is leaf node, return result.
            return result
        result += "(" + self.tree2str(root.left) + ")"              #Wrap the str of left substree and append it to result.
        if root.right:                                              #If root.right is not none, wrap the str of right substree and append it to result.
            result += "(" + self.tree2str(root.right) + ")"
        return result
