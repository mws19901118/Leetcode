# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:                                          #If root is empty, return true.
            return True
        leftw=root.left                                         #Use leftw to represent the left wing of root.
        rightw=root.right                                       #Use rightw to represent the right wing of root.
        while leftw!=None and rightw!=None:
            if leftw.val!=rightw.val:                           #If value of left wing node is not equal to value of right wing node, return false.
                return False
            elif (leftw.right!=None and rightw.left==None) or (leftw.right==None and rightw.left!=None):      #If one of right child of left wing node and left child of right wing node is empty and the other is not empty, return false.
                return False
            elif leftw.right!=None and rightw.left!=None and leftw.right.val!=rightw.left.val:                #If the value of right child of left wing node is not equal to the value of left child of right wing node, return false.
                return False
            else:
                virtualroot=TreeNode(-1)                        #Add a virtual root to right child of left wing node and left child of right wing node.
                virtualroot.left=leftw.right
                virtualroot.right=rightw.left
                if self.isSymmetric(virtualroot)==False:        #If the tree whose root is the virtual root is not symmertric, return false.
                    return False
                else:                                           #Otherwise, use the left child of left wing node to replace the left wing node and the right child of right wing node to replace the right wing node.
                    leftw=leftw.left
                    rightw=rightw.right
        if leftw!=None or rightw!=None:                         #If one of left wing node and right wing node is empty and the other is not empty, return false.
            return False
        else:                                                   #If the tree satisfy all the requirement, return true.
            return True
