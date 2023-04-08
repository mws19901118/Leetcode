"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clonedNodes = {}                                                            #Store cloned nodes.
        def cloneNode(node: 'Node') -> 'Node':                                      
            if not node:                                                            #If node is none, return none.
                return None
            if node.val in clonedNodes:                                             #If current node is already cloned, return the cloned node.
                return clonedNodes[node.val]
            clone = Node(node.val)                                                  #Cloud current node.
            clonedNodes[node.val] = clone                                           #Put cloned node into dictionary.
            clone.neighbors = [cloneNode(x) for x in node.neighbors]                #Recursively clone all neighbors.
            return clone                                                            #Return cloned node.
        return cloneNode(node)
