# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):                                       #The same idea with Closest Binary Search Tree Value II.
    def getPredecessor(self, predecessor, target):
        t = TreeNode(target)
        while len(predecessor) != 0:
            t = predecessor.pop()
            if t.val < target:
                break
        if t.val >= target:
            return target
        p = t.val
        t = t.left
        while t != None:
            predecessor.append(t)
            t = t.right
        return p
        
    def getSuccessor(self, successor, target):
        t = TreeNode(target)
        while len(successor) != 0:
            t = successor.pop()
            if t.val > target:
                break
        if t.val <= target:
            return target
        s = t.val
        t = t.right
        while t != None:
            successor.append(t)
            t = t.left
        return s
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        result = []
        predecessor = []
        successor = []
        while root != None:
            predecessor.append(root)
            successor.append(root)
            if root.val == target:
                return int(target)
            elif root.val > target:
                root = root.left
            else:
                root = root.right

        p = self.getPredecessor(predecessor, target)
        s = self.getSuccessor(successor, target)
        
        if p == target:
            return s
        elif s == target:
            return p
        else:
            if target - p < s - target:
                return p
            else:
                return s
