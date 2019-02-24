# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val > root.val:                          #If current node is none or current node's value is smaller than the new value, insert value above current value.
            newRoot = TreeNode(val)                                 #Create new tree node.
            newRoot.left = root                                     #Since new value is appended at the end, current node should be the left child of new node.
            return newRoot                                          #Return new node.
        else:
            root.right = self.insertIntoMaxTree(root.right, val)    #Otherwise, recursively check and update the right child.
            return root                                             #Return current node.
