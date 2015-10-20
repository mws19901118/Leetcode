# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        length=len(postorder)
        if length==0:
            return None
        root=TreeNode(postorder[length-1])                                          #Root is always the last element of postorder.
        if length>1:
            mid=inorder.index(postorder[length-1])                                  #Find the index of root in inorder.
            root.left=self.buildTree(inorder[:mid], postorder[:mid])                #The left child of root is from the start to mid in both postorder and inorder.
            root.right=self.buildTree(inorder[mid+1:], postorder[mid:length-1])     #The right child of root is from mid to length-1 in postorder while from mid+1 to length in inder.
        return root
