# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevelSum, result, level = float('-inf'), None, 1            #Initialize max sum of any level to be negative infinite; also initialize the result and level number.
        q = [root]                                                     #Initialize queue for BFS to be the tree root.
        while q:                                                       #BFS. 
            levelSum = 0                                               #Initialize the sum of current level.
            newq = []
            for x in q:                                                #Traverse nodes in current level.
                levelSum += x.val                                      #Add current node value to levelSum.
                if x.left:                                             #If x.left is not none, append x.left to newq.
                    newq.append(x.left)
                if x.right:                                            #If x.right is not none, append x.right to newq.
                    newq.append(x.right)
            
            if levelSum > maxLevelSum:                                 #Update result and maxLevelSum if necessary.
                result = level
                maxLevelSum = levelSum
            q = newq                                                   #Go to next level.
            level += 1
        return result
