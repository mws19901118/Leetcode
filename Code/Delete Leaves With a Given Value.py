# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:                                                                                 #If root is none, just return none.
            return None
        root.left = self.removeLeafNodes(root.left, target)                                          #Recursively remove target from left subtree.
        root.right = self.removeLeafNodes(root.right, target)                                        #Recursively remove target from right subtree.
        return None if not root.left and not root.right and root.val == target else root             #If root is leaf node and is target, return none; otherwise just return root.
