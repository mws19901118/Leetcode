# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root):                                               #Get the max path sum of current subtree and the max sum along the path from current node to leaf.
        if root.left is None and root.right is None:                    #If current node is leaf node, both the result is value of current node.
            return (root.val, root.val)
        elif root.left is not None and root.right is None:              #If current node only has left child, get the results from its left child.
            l = self.find(root.left)
            t = max(root.val, root.val + l[1])                          #The max sum along the path from current node to leaf is the max of current value and the sum of current value and that value of left child.
            return (max(l[0], t), t)                                    #The max path sum of current node is the max of that of left child and the max sum along the path from current node to leaf.
        elif root.left is None and root.right is not None:              #If current node only has right child, get the results from its right child.
            r = self.find(root.right)  
            t = max(root.val, root.val + r[1])                          #The max sum along the path from current node to leaf is the max of current value and the sum of current value and that value of right child.
            return (max(r[0], t), t)                                    #The max path sum of current node is the max of that of right child and the max sum along the path from current node to leaf.
        else:                                                           #If current has both child, get the results from them respectively.                         
            l = self.find(root.left)
            r = self.find(root.right)
            t = max(root.val, root.val + l[1], root.val + r[1])         #The max sum along the path from current node to leaf is the max of current value, the sum of current value and that value of left child and the sum of current value and that value of right child. 
            return (max(l[0], r[0], t, root.val + l[1] + r[1]), t)      #The max path sum of current node is the max of that of left child, that of right child and the max sum along the path from current node to leaf and the sum of current value and the max sum along the path from left child to leaf and the max sum along the path from right child to leaf.
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.find(root)[0]
