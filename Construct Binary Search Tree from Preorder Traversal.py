# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder == []:                                      #If preorder is empty, return none.
            return None
        root = TreeNode(preorder[0])                            #Create root node for the first element in preorder.
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:  #Find the subarray in preorder that all the elements are smaller than the value in root.
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])         #Construct left child from the subarray from last step.
        root.right = self.bstFromPreorder(preorder[i:])         #Construct right child from the remaining array.
        return root
