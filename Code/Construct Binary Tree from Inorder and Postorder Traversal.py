# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])                                                  #Root is always the last element of postorder.
        index = inorder.index(postorder[-1])                                            #Find the index of root in inorder.
        root.left = self.buildTree(inorder[:index], postorder[:index])                  #The left child of root is from the start to index in both postorder and inorder.
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])           #The right child of root is from index to length-1 in postorder while from index + 1 to length in inorder.
        return root
