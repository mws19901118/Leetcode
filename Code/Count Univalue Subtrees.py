# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, root):                                                                                     #Returen the number of univalue subtrees of current tree and if the current node is a root of univalue subtree.
        if root is None:
            return (0, False)
        if root.left is None and root.right is None:                                                          #If current node is a leaf node, it has 1 univalue subtree and is the root of that univalue subtree.
            return (1,True)
        elif root.left is None and root.right is not None:                                                    #If current node doesn't have left child but has right child, get the result from right child.
            r = self.find(root.right)
            if root.val == root.right.val and r[1] is True:                                                   #If current value equals right child's value and right child is root of a univalue subtree, there is a new univalue subtree and current node is its root.
                return (r[0] + 1, True)
            else:                                                                                             #Otherwise, there is no new univalue subtree.
                return (r[0], False)
        elif root.left is not None and root.right is None:                                                    #If current node doesn't have right child but has left child, get the result from left child.
            l = self.find(root.left)
            if root.val == root.left.val and l[1] is True:                                                    #If current value equals left child's value and left child is root of a univalue subtree, there is a new univalue subtree and current node is its root.
                return (l[0] + 1, True)
            else:                                                                                             #Otherwise, there is no new univalue subtree.
                return (l[0], False)
        else:
            r = self.find(root.right)                                                                         #If current node has both left child and right child, get results from both of them.
            l = self.find(root.left)
            if root.val == root.left.val and root.val == root.right.val and l[1] is True and r[1] is True:    #If current value equals both children's value and both children are root of a univalue subtreem there is a new univalue subtree and current node is its root.
                return (l[0] + r[0] + 1, True)
            else:                                                                                             #Otherwise, there is no new univalue subtree.
                return (l[0] + r[0], False)
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        t = self.find(root)                                                                                 #Recursively find the count of univalue subtrees.
        return t[0]
