# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, inorder: List[int], start: int, end: int, postorder: List[int], indexes) -> TreeNode:
        if start > end or not postorder:                                                #If start > end or postorder is empty, we cannot construct node, return None.
            return None
        node = TreeNode(postorder.pop())                                                #Initialize node with the last element in postorder; directly pop postorder because we always construct right child first so it's strictly traversing postorder backward.
        index = indexes[node.val]                                                       #Find the index of node.val in inorder.
        node.right = self.build(inorder, index + 1, end, postorder, indexes)            #Construct the right child of node with inorder[index + 1:end + 1] and postorder.
        node.left = self.build(inorder, start, index - 1, postorder, indexes)           #Construct the right child of node with inorder[start:index] and postorder.
        return node                                                                     #Return node.
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        indexes = {x: i for i, x in enumerate(inorder)}                                 #Cache integer indexes in inorder.
        return self.build(inorder, 0, len(inorder) - 1, postorder, indexes)             #Build binary tree.
