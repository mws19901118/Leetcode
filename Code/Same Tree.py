# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p==None and q==None:                               #If p and q are both empty, they are same.
            return True
        elif (p==None and q!=None) or (p!=None and q==None):  #If one is empty but the other is not, they are not same.
            return False
        else:
            if p.val!=q.val:                                  #If the value of p is not equal to the value of q, they are not same.
                return False
            else:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):       #If the left child of p and the left child of q are same, and the right child of p and right child of q are same, the value of p is equal to the value of q, they are same.
                    return False
