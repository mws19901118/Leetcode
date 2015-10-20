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
        if A.left==None and A.right!=None:                      #if A only have right child, return depth(A.right)+1
            return depth(A.right)+1
        elif A.left!=None and A.right==None:                    #if A only have left child, return depth(A.left)+1
            return depth(A.left)+1
        else:
            return min(depth(A.left),depth(A.right))+1

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return depth(root)
