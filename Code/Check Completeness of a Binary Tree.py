# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:                                                                  #BFS.
            newq = []                                                             #Initialize newq.
            noneNodeFound = False                                                 #Initialize if none node found in current level.
            for x in q:                                                           #Traverse current level.
                if not x:                                                         #If current node is none, set noneNodeFound to True and continue.
                    noneNodeFound = True
                    continue
                if noneNodeFound and x:                                           #If noneNodeFound and x is not none, return false.
                    return False
                newq.append(x.left)                                               #Append x.left to newq.
                newq.append(x.right)                                              #Append x.right to newq.
            if noneNodeFound and any(x for x in newq if x):                       #If noneNodeFound and any node in newq, return false.
                return False
            q = newq                                                              #Replace q with newq.
        return True                                                               #Return true.
