# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:                                #If root is none, return none.
            return None
        if root.left is None:                           #If root is leaf node, return root.
            return root
        p = root.left                                   #Recode the left child of root.
        t = self.upsideDownBinaryTree(root.left)        #Recursively flip the left child upside down and get the new root of left child.
        p.right = root                                  #Set the right child of original left child of root to be root.
        p.left = root.right                             #Set the left child of original left child of root to be right child of root.
        root.left = None                                #Reset the children of root to be none.
        root.right = None
        return t                                        #Return new root.
