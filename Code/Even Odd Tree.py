# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        level = 0                                                                                                                                  #Store the level.
        while q:                                                                                                                                   #BFS.
            lastValue = 1000001 if level & 1 else 0                                                                                                #Initialize a virtual last value: max value if is odd level; min value otherwise.
            newq = []
            for x in q:
                if (not level & 1 and not (x.val & 1 and x.val > lastValue)) or (level & 1 and not (not x.val & 1 and x.val < lastValue)):         #Check if value of each node meets the condition based on if current level is odd or even.
                    return False                                                                                                                   #If any node does not meet condition, directly return false.
                lastValue = x.val                                                                                                                  #Update lastValue.
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
            level += 1                                                                                                                             #Increase level.
        return True                                                                                                                                #Return true eventually.
