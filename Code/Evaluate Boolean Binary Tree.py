# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:                                                            #If root is leaf, return if its value is 1.
            return root.val == 1
        leftResult, rightResult = self.evaluateTree(root.left), self.evaluateTree(root.right)           #Get the result of left subtree and right subtree recursively.
        return (leftResult or rightResult) if root.val == 2 else (leftResult and rightResult)           #Return OR return or AND result depending on value of current root.
