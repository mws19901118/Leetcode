# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root==None:                                    #If root is none, return none.
            return None
        l=self.invertTree(root.left)                      #Record the answer of inverting left child of root.
        r=self.invertTree(root.right)                     #Record the answer of inverting right child of root.
        root.left=r                                       #Set the left child of root to be r.
        root.right=l                                      #Set the right child of root to be l.
        return root                                       #Return root.
