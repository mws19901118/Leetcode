# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        length=len(preorder)
        if length==0:
            return None
        root=TreeNode(preorder[0])                                            #Root is always the first element of preorder.
        if length>1:
            mid=inorder.index(preorder[0])                                    #Find the index of root in inorder.
            root.left=self.buildTree(preorder[1:mid+1], inorder[0:mid])       #The left child of root is from 1 to mid+1 in preorder while from 0 to mid in inder.
            root.right=self.buildTree(preorder[mid+1:], inorder[mid+1:])      #The right child of root is from mid+1 to the end in both preorder and inorder.
        return root
