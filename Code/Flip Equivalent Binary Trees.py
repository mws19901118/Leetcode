# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def beEqual(self, root1, root2):                                                                        #Judge if root1 and root2 are equivalent.
        if not root1 and not root2:                                                                         #If both are none, they are equivalent.
            return True
        elif not root1 or not root2 or root1.val != root2.val:                                              #If only one of them is none or their value is not same, they are not equivalent.
            return False
        else:                                                                                               #Otherwise they are equivalent.
            return True
        
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not self.beEqual(root1, root2):                                                                  #First judge if root1 and root2 are equivalent, return false.
            return False
        if not root1 and not root2:                                                                         #If both are none, return true.
            return True
        if self.beEqual(root1.left, root2.left) and self.beEqual(root1.right, root2.right):                 #If root1.left and root2.left are equivalent and root1.right and root2.right are equivalent, recursively compare root1.left, root2.left and root1.right, root2.right.
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        elif self.beEqual(root1.left, root2.right) and self.beEqual(root1.right, root2.left):               #If root1.left and root2.right are equivalent and root1.left and root2.right are equivalent, recursively compare root1.left, root2.right and root1.right, root2.left.
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        else:                                                                                               #Otherwise, return false.
            return False
