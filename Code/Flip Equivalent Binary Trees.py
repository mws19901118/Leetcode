# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:                                                                                                                                                                    #If both root1 and root2 are none, return true.
            return True
        if not root1 or not root2 or root1.val != root2.val:                                                                                                                                           #If exactly one is none or the values don't match, return false.
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))          #Then, the 2 children should match respectively, with or without flip.
