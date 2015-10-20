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
        a=depth(A.left)
        b=depth(A.right)
        if a==-1 or b==-1 or abs(a-b)>1:              #If the binary tree whose root is A, A's left child or A's right child, return -1.
            return -1
        return max(a,b)+1                             #If not, return the depth of A 

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if depth(root)!=-1:
            return True
        else:
            return False
