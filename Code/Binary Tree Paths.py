# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def backtracking(self, stack, node, result):                      #Backtracking.
        if node.left is None and node.right is None:                  #If reach leaf node, generate the path string and append it to result.
            s = ""
            for i in range(len(stack)):
                s += str(stack[i].val) + "->"
            s += str(node.val)
            result.append(s)
        else:
            stack.append(node)                                        #Append node to stack.
            if node.left is not None:                                 #If left child is not none, dfs through left node.
                self.backtracking(stack, node.left, result)
            if node.right is not None:                                #After finishing dfs left node, dfs through right node if it is not none.
                self.backtracking(stack, node.right, result)
            stack.pop()                                               #Pop stack.
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        stack = []
        result = []
        self.backtracking(stack, root, result)
        return result
