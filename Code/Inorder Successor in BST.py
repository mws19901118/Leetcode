# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        cursor = root
        path = []                             #Use a stack to store all the nodes on the path from root to p whose value is larger than that of p.
        while cursor is not p:
            if p.val > cursor.val:
                cursor = cursor.right
            elif p.val < cursor.val:
                path.append(cursor)
                cursor = cursor.left
        if p.right is not None:               #If p has right child, return the leftmost node of the right child of p.
            cursor = p.right
            while cursor.left is not None:
                cursor = cursor.left
            return cursor
        else:                                 #Otherwise, if stack is not empty, pop the stack and return the node.
            if path != []:
                return path.pop()
            else:                             #If stack is empty, there is no successor, return none.
                return None
