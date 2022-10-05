# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:                                                                                        #If root is none, return none.
            return None
        if depth == 1:                                                                                      #If depth is 1, insert node as its left and right children then return root.
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
            return root
        self.traverse(root.left, val, depth - 1)                                                            #Recursively traverse left subtree with depth - 1.
        self.traverse(root.right, val, depth - 1)                                                           #Recursively traverse right subtree with depth - 1.
        return root                                                                                         #Return root.

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return TreeNode(val, root, None) if depth == 1 else self.traverse(root, val, depth - 1)             #If depth is 1, return the new root with current root as its left; otherwise, return the result from traverse.
