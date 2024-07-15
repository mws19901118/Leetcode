# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        def findNode(path: List[int], node: Optional[TreeNode]) -> None:          #Traverse tree and find the path from root to p and q respectively.
            if not node:                                                          #If node is none, return.
                return
            path.append(node.val)                                                 #Append node.val to path.
            if node.val == p:                                                     #If node.val equals to p, extend path to pPath.
                pPath.extend(path)
            if node.val == q:                                                     #If node.val equals to q, extend path to qPath.
                qPath.extend(path)
            findNode(path, node.left)                                             #Traverse left subtree.
            findNode(path, node.right)                                            #Traverse right subtree.
            path.pop()                                                            #Pop path.
        
        pPath, qPath = [], []                                                     #Initialize pPath and qPath.
        findNode([], root)                                                        #Traverse tree.
        i, j = 0, 0
        while i < len(pPath) and j < len(qPath) and pPath[i] == qPath[j]:         #Traverse pPath and qPath simultaneously until they diverge.
            i += 1
            j += 1
        return len(pPath) - i + len(qPath) - j                                    #The sum of rest length is the distance.
