# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        depth = 0
        while q:                                                          #BFS.
            newq = []
            for i, x in enumerate(q):
                if depth & 1 and i < len(q) // 2:                         #Reverse the level if depth is odd.
                    x.val, q[-(i + 1)].val = q[-(i + 1)].val, x.val
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
            depth += 1
        return root
