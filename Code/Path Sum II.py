# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root: TreeNode, targetSum: int, stack: List[int], result: List[List[int]]) -> None:
        if not root:                                                                                        #If root is none, return.
            return
        stack.append(root.val)                                                                              #Append root.val to stack.
        if not root.left and not root.right and targetSum == root.val:                                      #If root is leaf node and targetSum equals root.val, append deepcopy of stack to result.
            result.append(deepcopy(stack))
        else:                                                                                               #Otherwise, keep DFS on root.left and root.right for targetSum - root.val.
            self.DFS(root.left, targetSum - root.val, stack, result)
            self.DFS(root.right, targetSum - root.val, stack, result)
        stack.pop()                                                                                         #Pop stack.
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []                                                                                         #Initialize result.
        self.DFS(root, targetSum, [], result)                                                               #DFS.
        return result
