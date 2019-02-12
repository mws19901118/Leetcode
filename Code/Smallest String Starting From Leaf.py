# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.minTrace = [26]                                      #Initialize the minimal trace. Since the max value of node is 25, we just use one 26.
        
    def DFS(self, node, trace):                                   #DFS.
            trace.append(node.val)                                #Append current node value to trace.
            if node.left:                                         #DFS left child.
                self.DFS(node.left, trace)
            if node.right:                                        #DFS right child.
                self.DFS(node.right, trace)
            if not node.left and not node.right:                  #If current node is leaf node, update minTrace with the smaller of minTrace and reverse of trace.
                self.minTrace = min(self.minTrace, trace[::-1])
            trace.pop()
            
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':        
        self.DFS(root, [])                                        #Start DFS from root node with empty trace.
        result = ""
        for x in self.minTrace:                                   #Convert minTrace to result.
            result += chr(ord('a') + x)
        return result
