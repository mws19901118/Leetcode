# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:                                                                                     #If p and q are both empty, they are same.
            return True
        elif (p is not None and q is None) or (p is None and q is not None):                                            #If one is empty but the other is not, they are not same.
            return False
        elif p.val != q.val:                                                                                            #If the value of p is not equal to the value of q, they are not same.
            return False
        else:                                                                                                           #If the left child of p and the left child of q are same, and the right child of p and right child of q are same, the value of p is equal to the value of q, they are same.
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
