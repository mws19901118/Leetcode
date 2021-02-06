# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        result = []
        while q:                                #Do the binary tree level order traverse using BFS.
            newq = []
            result.append(q[-1].val)            #Append value of the last node of each level to result.
            for x in q:
                if x.left:
                    newq.append(x.left)
                if x.right:
                    newq.append(x.right)
            q = newq
        return result
