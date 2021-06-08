# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preorder: List[int], s1: int, e1: int, inorder: List[int], s2: int, e2: int, indexes: dict) -> TreeNode:        #Helper to build tree with preorder[s1:e1 + 1], inorder[s2:e2 + 1] and cached indexes of integers in inorder.
        if s1 > e1 or s2 > e2:                                                                                                      #If the slice of preorder or inorder is empty, return none.
            return None
        node = TreeNode(preorder[s1])                                                                                               #Create a node with the first integer in the preorder slice.
        index = indexes[preorder[s1]]                                                                                               #Find the corresponding index in inorder.
        node.left = self.build(preorder, s1 + 1, s1 + (index - s2), inorder, s2, index - 1, indexes)                                #Construct the left child. For preorder, the offset of left child is (index - s2).
        node.right = self.build(preorder, s1 + (index - s2) + 1, e1, inorder, index + 1, e2, indexes)                               #Construct the right child.
        return node                                                                                                                 #Return node.
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexes = {x: i for i, x in enumerate(inorder)}                                                                             #Cache indexes of integers in inorder.
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, indexes)                                    #Return constructed binary tree.
