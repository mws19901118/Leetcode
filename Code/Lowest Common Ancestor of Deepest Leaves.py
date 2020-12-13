# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderTraverse(self, root: TreeNode, depth: int, depthDict: dict) -> None:                    #Find the depth of each node using pre-order traverse.
        if root is None:
            return
        depthDict[depth].append(root.val)                                                               #Use a dict to store the node value, key is depth.
        self.preOrderTraverse(root.left, depth + 1, depthDict)
        self.preOrderTraverse(root.right, depth + 1, depthDict)
    
    def postOrderTraverse(self, root: TreeNode, deepestNodes: set, result: List[TreeNode]) -> bool:     #Find if a node has deepest node in its subtree using post-order traverse.
        if root is None:                                                                                #If root is none, return false.
            return False    
        left = self.postOrderTraverse(root.left, deepestNodes, result)                                  #Check if left subtree contains deepest node.
        right = self.postOrderTraverse(root.right, deepestNodes, result)                                #Check if right subtree contains deepest node.
        if (left and right) or root.val in deepestNodes:                                                #If root is one of deepest nodes or left subtree and right subtree both contains deepest node, add current root to results. 
            result.append(root)
        return left or right or root.val in deepestNodes                                                #Return left or right or root is one of the deepest nodes.
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        depthDict = defaultdict(list)
        self.preOrderTraverse(root, 0, depthDict)                                                       #Pre-order traverse.
        maxDepth = max(d for d in depthDict)                                                            #Get the max depth.
        deepestNodes = set(depthDict[maxDepth])                                                         #Store deepest nodes value in a set.
        result = []                                                                                     #Use a list to store all possible nodes whose subtree contain all deepest nodes.
        self.postOrderTraverse(root, deepestNodes, result)                                              #Post-order traverse.
        return result[-1]                                                                               #Return the last element in result.
