# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:                                    #Traverse 2 trees simultaneously to determine if they are symmetric to each other.
        if not left and not right:                                                                                      #If both are none, return true.
            return True
        elif (left and not right) or (not left and right) or left.val != right.val:                                     #If only one of them is none or the values don't match, return false.
            return False
        return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)                          #Return true if both left subtree of left and right subtree of right are symmetric and right subtree of left and left subtree of right are symmetric.

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root.left, root.right)                                                                     #Traverse from root recursively.
