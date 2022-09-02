# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        average = []                              #Initialize average for each level.
        q = [root]                                #Add root to queue.
        while q:                                  #BFS.
            newq = []                             #Initialize new queue.
            levelSum = 0                          #Initialize level sum.
            for x in q:                           #For each node in queue, add its value to level sum.
                levelSum += x.val
                if x.left:                        #If left child of current node is not none, append it to new queue.
                    newq.append(x.left)
                if x.right:                       #If right child of current node is not none, append it to new queue.
                    newq.append(x.right)
            average.append(levelSum / len(q))     #Calculate level average and append it to average list.
            q = newq                              #Replace queue with new queue.
        return average
