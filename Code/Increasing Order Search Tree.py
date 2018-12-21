# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        order = []
        self.traverse(root, order)
        newRoot = TreeNode(order[0])            #Create new tree.
        itr = newRoot
        for i in range(1, len(order)):
            itr.right = TreeNode(order[i])
            itr = itr.right
        return newRoot
        
    def traverse(self, root, order):            #Traverse the tree and record the values in order.
        if root is None:
            return
        self.traverse(root.left, order)
        order.append(root.val)
        self.traverse(root.right, order)
