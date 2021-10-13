# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:                                                #If preorder is empty, return none.
            return None
        root = TreeNode(preorder[0])
        index = bisect.bisect(preorder, root.val, 1, len(preorder))     #Binary search for the index of preorder[0] in the rest of array.
        root.left = self.bstFromPreorder(preorder[1:index])             #Construct left child from the subarray from last step.
        root.right = self.bstFromPreorder(preorder[index:])             #Construct right child from the remaining array.
        return root
