# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root, minV, maxV) -> bool:
        if not root:
            return True
        if root.val <= minV or root.val >= maxV:                                                            #If value of current node is smaller than min valid value or larger than max valid value, return false.
            return False
        return self.isValid(root.left, minV, root.val) and self.isValid(root.right, root.val, maxV)         #The value of left child should be smaller than current value and the value of right child should be larger than current value; otherwise it is not a valid BST.
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, -0xFFFFFFFF, 0xFFFFFFFF)
