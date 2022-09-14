# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root: TreeNode, path: int, masks: dict) -> int:
        if not root:                                                                    #If root is none, return 0.
            return 0
        path ^= masks[root.val]                                                         #XOR path with the mask of value of current node.
        if not root.left and not root.right:                                            #If current node is leaf, check if path is exponent of 2. If so, the path is pseudo-palindromic and return 1; otherwise, return 0.
            return int(path & (path - 1) == 0)
        return self.DFS(root.left, path, masks) + self.DFS(root.right, path, masks)     #If current node is not leaf, return the sum of DFS results of left child and right child.
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        masks = {i + 1: 1 << i for i in range(9)}                                       #Use a 9 bits int to represent the parity of count of all numbers in path. So, create a bit mask 2 ^ x at each number x.    
        return self.DFS(root, 0, masks)                                                 #DFS fron root.
