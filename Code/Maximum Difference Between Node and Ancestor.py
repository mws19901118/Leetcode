# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int, int):                                                                                                  #Traverse binary tree from node, return min value, max value and max difference between node and ancestor in this binary tree.
            if not root.left and not root.right:                                                                                                                    #If root is leaf, return current root node value as min value and max value and 0 as max difference between node and ancestor.
                return root.val, root.val, 0
            elif not root.left and root.right:                                                                                                                      #If left child is none, traverse right subtree and calculate min value, max value and max difference between node and ancestor then return.
                r = traverse(root.right)
                return min(r[0], root.val), max(r[1], root.val), max(r[2], abs(root.val - r[0]), abs(root.val - r[1]))
            elif root.left and not root.right:                                                                                                                      #If right child is none, traverse left subtree and calculate min value, max value and max difference between node and ancestor then return.
                l = traverse(root.left)
                return min(l[0], root.val), max(l[1], root.val), max(l[2], abs(root.val - l[0]), abs(root.val - l[1]))
            else:                                                                                                                                                   #Otherwise traverse both left and right subtree and calculate min value, max value and max difference between node and ancestor then return.
                l, r = traverse(root.left), traverse(root.right)
                return min(l[0], r[0], root.val), max(l[1], r[1], root.val), max(l[2], r[2], abs(root.val - min(l[0], r[0])), abs(root.val - max(l[1], r[1])))
    
        return traverse(root)[2]                                                                                                                                        #Return max difference between node and ancestor in this binary tree.                                                                                                                     
