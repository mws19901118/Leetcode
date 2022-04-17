# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, root: TreeNode) -> (TreeNode, TreeNode):          #Convert BST and return root and leaf.
        newRoot, newLeaf = None, None                                   #Initialize new root and new leaf.
        if root.left:                                                   #If root has left child, convert it's left subtree and update newRoot and newLeaf.
            newRoot, newLeaf = self.convert(root.left)
            root.left = None                                            #Set root.left to none.
            newLeaf.right, newLeaf = root, root                         #Point newLeaf.right to root and then point newLeaf to root.
        else:                                                           #Otherwise, newRoot and newLeaf is root.
            newRoot, newLeaf = root, root
        if root.right:                                                  #If root has right child, convert it's right subtree and update newLeaf.
            newLeaf.right, newLeaf = self.convert(root.right)
        return newRoot, newLeaf                                         #Return newRoot and newLeaf.
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.convert(root)[0]                                    #Return the root after convertion.
