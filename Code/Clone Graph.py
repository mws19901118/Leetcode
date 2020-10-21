"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        newNode = Node(node.val)                                                        #Initalize the copy of given node.
        visited = set()                                                                 #Record visited nodes.
        valToNodeMap = {node.val: newNode}                                              #Use dict to map node by its value.
        q = [node]                                                                      #Initialize queue for BFS.
        while q:                                                                        #BFS.
            newq = []                                                                   #Initialize new queue.
            for x in q:                                                                 #Traverse through nodes in queue.
                if x in visited:                                                        #If current node is visited, skip it.
                    continue
                for y in x.neighbors:                                                   #Traverse through nodes in the neighbors of current node.
                    if y.val not in valToNodeMap:                                       #If this neighbor is not in map, initialize a copy and add to map.
                        valToNodeMap[y.val] = Node(y.val)
                    valToNodeMap[x.val].neighbors.append(valToNodeMap[y.val])           #Append the copy of neighbor to the neighbors of copy of current node.
                    newq.append(y)                                                      #Append neighbor to new queue.
                visited.add(x)                                                          #Add current node to visited.
            q = newq                                                                    #Replace queue with new queue for next iteration.
        return newNode
