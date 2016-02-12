# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:                                              #If root is none, return 0.
            return 0
        maxnodes = [0]                                                #Store the number of nodes of largest BST subtree.
        
        def isBST(root, maxnodes):                                    #Judge if the subtree whose root is current node is a BST, return a tuple(The boolean indicating if subtree is a BST, The min value of subtree, The max value of subtree, The number of nodes of subtree).
            if root.left is None and root.right is None:              #If root is a leaf node, it is a BST.
                maxnodes[0] = max(maxnodes[0], 1)
                return (True, root.val, root.val, 1)
            elif root.left is not None and root.right is None:        #If root only has left child, its left child should be BST and value of root should be greater than the max value of left subtree.
                l = isBST(root.left, maxnodes)
                if l[0] is False or root.val <= l[2]:
                    return (False, -1, -1, -1)
                else:
                    maxnodes[0] = max(maxnodes[0], l[3] + 1)
                    return (True, l[1], root.val, l[3] + 1)
            elif root.left is None and root.right is not None:        #If root only has right child, its right child should be BST and value of root should be smaller than the min value of right subtree.
                r = isBST(root.right, maxnodes)
                if r[0] is False or root.val >= r[1]:
                    return (False, -1, -1, -1)
                else:
                    maxnodes[0] = max(maxnodes[0], r[3] + 1)
                    return (True, root.val, r[2], r[3] + 1)
            else:                                                     #If root has both children, both of them should be BST and value of root should be greater than the max value of left subtree and smaller than the min value of right subtree.
                l = isBST(root.left, maxnodes)
                r = isBST(root.right, maxnodes)
                if l[0] is False or r[0] is False or root.val <= l[2] or root.val >= r[1]:
                    return (False, -1, -1, -1)
                else:
                    maxnodes[0] = max(maxnodes[0], l[3] + r[3] + 1)
                    return (True, l[1], r[2], l[3] + r[3] + 1)
        
        t = isBST(root, maxnodes)                                     #Recursively traverse the tree.
        return maxnodes[0]                                            #Return the number of nodes of largest BST.
