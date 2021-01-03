# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:                                                                                  #If cloned is none, return none.
            return None
        if cloned.val == target.val:                                                                    #If value of cloned equals value of target, return cloned.
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)                                   #Find target in the left subtree of cloned.
        return self.getTargetCopy(original.right, cloned.right, target) if left is None else left       #If found, return result; otherwise return the result of finding target in the right subtree of cloned.
