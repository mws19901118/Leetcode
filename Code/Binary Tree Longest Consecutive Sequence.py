# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self, root):                                                             #Return the longest consecutive sequence in current tree and the longest consecutive sequence which begins with current node.
        if root is None:                                                                #If current node is none, return (0, 0).
            return (0, 0)
        if root.left is None and root.right is None:                                    #If current node is leaf node, return (1, 1).
            return (1, 1)
        elif root.left is not None and root.right is None:                              #If current node only has left child, find the result of its left child recursively.
            l = self.search(root.left)
            if root.val == root.left.val - 1:                                           #If current value plus 1 equals the value of its left child, the new longest consecutive sequence is max(l[0], l[1] + 1).
                return (max(l[0], l[1] + 1), l[1] + 1)
            else:                                                                       #Otherwise, return (l[0], 1).
                return (l[0], 1)
        elif root.left is None and root.right is not None:                              #If current node only has right child, find the result of its right child recursively.
            r = self.search(root.right)
            if root.val == root.right.val - 1:                                          #If current value plus 1 equals the value of its right child, the new longest consecutive sequence is max(r[0], r[1] + 1).
                return (max(r[0], r[1] + 1), r[1] + 1)
            else:                                                                       #Otherwise, return (r[0], 1).
                return (r[0], 1)
        else:                                                                           #If current node has both children, find the result of both children.
            l = self.search(root.left)
            r = self.search(root.right)
            if root.val == root.left.val - 1 and root.val == root.right.val - 1:        #If current value plus 1 equals the values of both children, the new longest consecutive sequence is max(l[0], l[1] + 1, r[0], r[1] + 1).
                return (max(l[0], l[1] + 1, r[0], r[1] + 1), max(l[1] + 1, r[1] + 1))
            elif root.val == root.left.val - 1 and root.val != root.right.val - 1:      #If current value plus 1 only equals the value of its left child, the new longest consecutive sequence is max(l[0], l[1] + 1, r[0]).
                return(max(l[0], l[1] + 1, r[0]), l[1] + 1)
            elif root.val != root.left.val - 1 and root.val == root.right.val - 1:      #If current value plus 1 only equals the value of its right child, the new longest consecutive sequence is max(r[0], r[1] + 1, 1[0]).
                return(max(r[0], r[1] + 1, l[0]), r[1] + 1)
            else:                                                                       #Otherwise, return (max(l[0], r[0]), 1).
                return (max(l[0], r[0]), 1)
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.search(root)[0]
