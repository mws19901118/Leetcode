# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        q = [root]                                  #Store nodes in current level.
        while q:                                    #BFS while q is not empty.
            level = []                              #Store the values in current level.
            newq = []                               #Store nodes in current level.
            for x in q:
                level.append(x.val)                 #Add value to level.
                if x.left:                          #If node has left child, add it to newq.
                    newq.append(x.left)
                if x.right:                         #If node has right child, add it to newq.
                    newq.append(x.right)
            q = newq                                #Repalce q with newq.
            result.append(level)                    #Add level to result.
        return result
