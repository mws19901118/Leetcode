# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []                                                                      #Initialize paths.

        def DFS(root: Optional[TreeNode], stack: List[int], remain: int):               #DFS.
            if not root:                                                                #If root is none, return.
                return
            stack.append(root.val)                                                      #Append root.val to stack.
            remain -= root.val                                                          #Substract root.val from remain.
            if not root.left and not root.right and not remain:                         #If root is leaf node and remain is 0, we wound a path sum so append the deepcopy of stack to paths.
                paths.append(deepcopy(stack))
            DFS(root.left, stack, remain)                                               #Keep DFS in root.left.
            DFS(root.right, stack, remain)                                              #Keep DFS is root.right.
            stack.pop()                                                                 #Pop stack.
        
        DFS(root, [], targetSum)                                                        #Start DFS from root.
        return paths                                                                    #Return paths.
