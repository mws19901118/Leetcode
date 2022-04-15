# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:                                                #If root is none, return none.
            return None
        if root.val < low:                                          #If root is smaller than low, return the trimmed right subtree.
            return self.trimBST(root.right, low, high)
        elif root.val > high:                                       #If root is larger than high, return the trimmed left subtree.
            return self.trimBST(root.left, low, high)
        else:                                                       #If root is between low and high, trim left subtree and right subtree respectively and then return root.
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
