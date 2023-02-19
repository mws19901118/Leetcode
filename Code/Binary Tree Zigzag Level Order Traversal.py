# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                                                                        #If root is none, return empty list.
            return []
        result = []                                                                         #Initialize result.
        q = [root]                                                                          #Initialize queue.
        while q:                                                                            #Level order BFS.
            level = []
            newq = []
            for x in q:
                level.append(x.val)
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
            result.append(level[::-1] if len(result) & 1 else level)                        #Append current level to result, the order depends on which level it's in.
        return result
