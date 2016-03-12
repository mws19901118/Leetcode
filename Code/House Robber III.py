# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob0(self, root, dict0, dict1):                                                 #Calculate the max value not robbing current house.
        if root is None:
            return 0
        if root in dict0:
            return dict0[root]
        if root.left is None and root.right is None:
            ans = 0
        elif root.left is not None and root.right is None:
            ans = max(self.rob0(root.left, dict0, dict1), self.rob1(root.left, dict0, dict1))
        elif root.left is None and root.right is not None:
            ans = max(self.rob0(root.right, dict0, dict1), self.rob1(root.right, dict0, dict1))
        else:
            ans = max(self.rob0(root.left, dict0, dict1), self.rob1(root.left, dict0, dict1)) + max(self.rob0(root.right, dict0, dict1), self.rob1(root.right, dict0, dict1))
        dict0[root] = ans
        return ans
    def rob1(self, root, dict0, dict1):                                                 #Calculate the max value robbing current house.
        if root is None:
            return 0
        if root in dict1:
            return dict1[root]
        if root.left is None and root.right is None:
            ans = root.val
        elif root.left is not None and root.right is None:
            ans = root.val + self.rob0(root.left, dict0, dict1)
        elif root.left is None and root.right is not None:
            ans = root.val + self.rob0(root.right, dict0, dict1)
        else:
            ans = root.val + self.rob0(root.left, dict0, dict1) + self.rob0(root.right, dict0, dict1)
        dict1[root] = ans
        return ans
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        dict0 = {}                                                                      #Use dict0 to store intermedia results for rob0.
        dict1 = {}                                                                      #Use dict1 to store intermedia results for rob1.
        return max(self.rob0(root, dict0, dict1), self.rob1(root, dict0, dict1))        #Return the max of rob0(root) and rob1(root).
