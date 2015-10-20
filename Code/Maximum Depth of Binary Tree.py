# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def depth(A):
    if A==None:
        return 0
    else:
        return max(depth(A.left),depth(A.right))+1

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return depth(root)
