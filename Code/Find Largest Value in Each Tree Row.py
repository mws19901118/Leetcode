# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                                #If root is none, return empty list.
            return []
        result = []
        q = [root]
        while q:                                    #BFS.
            newq = []                               #Initialize next row.
            levelMax = -inf                         #Initialize current row max value.
            for x in q:                             #Traverse all nodes in current row.
                levelMax = max(levelMax, x.val)     #Update levelMax if necessary.
                if x.left:                          #Append x.left to newq if it is not none.
                    newq.append(x.left)
                if x.right:                         #Append x.right to newq if it is not none.
                    newq.append(x.right)
            result.append(levelMax)                 #Append largest value in current row to result.
            q = newq                                #Go to next row.
        return result
