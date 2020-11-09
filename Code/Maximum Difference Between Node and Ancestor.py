# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode) -> tuple:                                                                                                                  #Traverse binary tree from node, return min value, max value and max difference between node and ancestor in this binary tree.
        if root.left is None and root.right is None:                                                                                                              #If root is leaf, return current root node value as min value and max value and 0 as max difference between node and ancestor
            return root.val, root.val, 0
        elif root.left is None and root.right is not None:                                                                                                        #If left child is none, traverse right subtree and calculate min value, max value and max difference between node and ancestor then return.
            r = self.traverse(root.right)
            return min(r[0], root.val), max(r[1], root.val), max(r[2], abs(root.val - r[0]), abs(root.val - r[1]))
        elif root.left is not None and root.right is None:                                                                                                        #If right child is none, traverse left subtree and calculate min value, max value and max difference between node and ancestor then return.
            l = self.traverse(root.left)
            return min(l[0], root.val), max(l[1], root.val), max(l[2], abs(root.val - l[0]), abs(root.val - l[1]))
        else:                                                                                                                                                     #Otherwise traverse both left and right subtree and calculate min value, max value and max difference between node and ancestor then return.
            l, r = self.traverse(root.left), self.traverse(root.right)
            return min(l[0], r[0], root.val), max(l[1], r[1], root.val), max(l[2], r[2], abs(root.val - min(l[0], r[0])), abs(root.val - max(l[1], r[1])))
    def maxAncestorDiff(self, root: TreeNode) -> int:
        result = self.traverse(root)
        return result[2]                                                                                                                                          #Return max difference between node and ancestor in this binary tree.
