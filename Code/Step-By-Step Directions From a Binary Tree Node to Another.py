# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findNode(path: List[str], node: Optional[TreeNode]) -> None:                          #Find the steps from root to startValue and destValue.
            if node.val == startValue:                                                            #If node.val equals to startValue, extend path to startPath.
                startPath.extend(path)
            if node.val == destValue:                                                             #If node.val equals to destValue, extend path to destPath.
                destPath.extend(path)
            if node.left:                                                                         #If node.left is not none, append 'L' to path and keep dfs and pop path after dfs.
                path.append('L')
                findNode(path, node.left)
                path.pop()
            if node.right:                                                                        #If node.right is not none, append 'R' to path and keep dfs and pop path after dfs.
                path.append('R')
                findNode(path, node.right)
                path.pop()
        
        startPath, destPath = [], []                                                              #Initialize startPath and destPath.
        findNode(['N'], root)                                                                     #Traverse tree.
        i, j = 0, 0
        while i < len(startPath) and j < len(destPath) and startPath[i] == destPath[j]:           #Traverse startPath and destPath simultaneously until they diverge.
            i += 1
            j += 1
        return 'U' * (len(startPath) - i) + "".join(destPath[j:])                                 #Go up from start value (len(startPath) - i) times then follow the steps in destPath[j:].
