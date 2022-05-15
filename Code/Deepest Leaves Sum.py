# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while True:                                           #Do binary tree level order traversal.
            newq = []
            leavesSum = 0
            for x in q:
                if not x.left and not x.right:                #Calculate the sum of leaves in current level.
                    leavesSum += x.val
                for y in [x.left, x.right]:
                    if y:
                        newq.append(y)
            if not newq:                                      #If reaches the last level, return leavesSum. 
                return leavesSum
            q = newq                                          #Go tot next level.
