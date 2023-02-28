# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        structures = Counter()                                                                #Initialize a counter to store subtree structure.
        result = []                                                                           #Initialize result list.
        def dfs(root: Optional[TreeNode]) -> str:                                             #DFS to return serialized format of subtree.
            if not root:                                                                      #If root is none, return '#' as none.
                return '#'
            serialization = str(root.val) + ',' + dfs(root.left) + ',' + dfs(root.right)      #Get the serialized format of current subtree.
            if structures[serialization] == 1:                                                #If already seen this structure once, append current to result.
                result.append(root)
            structures[serialization] += 1                                                    #Increase its count.
            return serialization                                                              #Return serialized format.

        dfs(root)                                                                             #DFS from root.
        return result
