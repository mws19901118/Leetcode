# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):                          #Do the binary tree level order traverse using BFS.
        q = []
        if root is not None:
            q.append(root)
        result = []
        while q:
            nextq = []
            for x in q:
                if x.left is not None:
                    nextq.append(x.left)
                if x.right is not None:
                    nextq.append(x.right)
            result.append(q[-1].val)                        #Append value of the last node of each level to result.
            q = nextq
        return result
