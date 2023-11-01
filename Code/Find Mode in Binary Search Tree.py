# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()                                        #Count each number.
        def traverse(node: Optional[TreeNode]):                  #DFS.
            if not node:
                return
            count[node.val] += 1                                 #Update count.
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)                                           #Traverse from root.
        maxV = max(count.values())                               #Find max count.
        return [x for x in count if count[x] == maxV]            #Return modes.
            
