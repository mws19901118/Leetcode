# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:                                            #If root is none, create a tree node with val and let it be root.
            root = TreeNode(val)
        elif root.val > val:                                        #If root.val > val, recursively insert val in left subtree and update the left child of root.
            root.left = self.insertIntoBST(root.left, val)
        else:                                                       #If root.val < val, recursively insert val in right subtree and update the right child of root.
            root.right = self.insertIntoBST(root.right, val)
        return root                                                 #Return root.
