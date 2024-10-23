# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum, q = [], [root]                                                                            #BFS to compute the sum of each level.
        while q:
            levelSum.append(0)
            newq = []
            for x in q:
                levelSum[-1] += x.val
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
        level, q = 0, [(root, root.val)]                                                                    #BFS again to update value of each node.
        while q:
            newq = []
            for x, deduct in q:
                x.val = levelSum[level] - deduct                                                            #New value is the sum of current value deducted by the sum of itself and its direct sibling.
                next_deduct = (0 if not x.left else x.left.val) + (0 if not x.right else x.right.val)       #Calculate the sum of children of current node.
                if x.left:                                                                                  #If x.left is not none, pass x.left and sum of children of x to next iteration of BFS.
                    newq.append((x.left, next_deduct))
                if x.right:                                                                                 #If x.right is not none, pass x.right and sum of children of x to next iteration of BFS.
                    newq.append((x.right, next_deduct))
            q = newq
            level += 1
        return root                                                                                         #Return root.
