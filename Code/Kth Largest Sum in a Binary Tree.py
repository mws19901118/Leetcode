# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSum, q = [], [root]              #BFS to compute the sum of each level.
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
        if len(levelSum) < k:                #If fewer than k level, return -1.
            return -1
        levelSum.sort(reverse = True)        #Sort level sum in desending order.
        return levelSum[k - 1]               #Return the levelSum[k - 1].
