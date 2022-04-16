# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumUp(self, root: TreeNode, greater: int) -> int:           #Sum up keys greater than or equal to current root.val.
        if not root:                                                #If root is none, return greater.
            return greater
        root.val += self.sumUp(root.right, greater)                 #Sum up right subtree and add tje result to root.val.
        return self.sumUp(root.left, root.val)                      #Sum up left subtree with root.val as greater and return.
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sumUp(root, 0)                                         #Recursively convert the entire tree.
        return root                                                 #Return root.
