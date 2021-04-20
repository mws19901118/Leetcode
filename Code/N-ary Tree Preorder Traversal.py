"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []                                 #Initialize result to be an empty list.
        if root is None:                            #If root is none, return result.
            return result
        stack = [root]                              #Initialize stack with root.
        while stack:                                #DFS.
            node = stack.pop()                      #Pop stack.
            result.append(node.val)                 #Append val of current node to result.
            stack.extend(node.children[::-1])       #Push the reverse order of children of current node to stack.
        return result                               #Return result.
