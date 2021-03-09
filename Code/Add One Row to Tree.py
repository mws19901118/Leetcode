# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:                                                  #Handle the case where d == 1: add a new root and set its left child to original root.
            newRoot = TreeNode(v, root, None)
            return newRoot
        q = [root]
        l = 1
        while l < d - 1:                                            #Traverse binary tree in level order until current level is d - 1.
            newq = []
            for x in q:
                if x.left is not None: newq.append(x.left)
                if x.right is not None: newq.append(x.right)
            q = newq
            l += 1
        for x in q:                                                 #Insert new level under current level.
            x.left = TreeNode(v, x.left, None)                      #Left child of current node becomes the left child of new left child of current node.
            x.right = TreeNode(v, None, x.right)                    #Right child of current node becomes the right child of new right child of current node.
        return root                                                 #Return root.
