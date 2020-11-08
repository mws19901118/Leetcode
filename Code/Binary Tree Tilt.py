# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode) -> tuple:                                #Traverse the binary tree, return the sum of tilt and sum of subtree value.
        if root is None:                                                        #If root is none, return 0 and 0.
            return 0, 0
        l, r = self.traverse(root.left), self.traverse(root.right)              #Traverse left and right subtree.
        return l[0] + r[0] + abs(l[1] - r[1]), root.val + l[1] + r[1]           #Calculate sum of tile and sum of subtree and then return.
    def findTilt(self, root: TreeNode) -> int:
        result = self.traverse(root)                                            #Get the traverse result of the entire binary tree.
        return result[0]                                                        #Return the sum of tile.
