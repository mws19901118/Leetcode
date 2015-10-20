# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def isValid(root,minV,maxV):
            if root==None:
                return True
            if root.val<=minV or root.val>=maxV:                      #If value of current node is smaller than min valid value or larger than max valid value, return false.
                return False
            return isValid(root.left,minV,root.val) and isValid(root.right,root.val,maxV)       #The value of left child should be smaller than current value and the value of right child should be larger than current value; otherwise it is not a valid BST.
        
        minV=-0xFFFFFFFF
        maxV=0xFFFFFFFF
        return isValid(root, minV, maxV)
