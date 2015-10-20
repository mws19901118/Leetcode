# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: 
            return None
        dictionary={node.label:UndirectedGraphNode(node.label)}                     #dictionary
        currentQueue=collections.deque()                                            #system deque
        currentQueue.append(node)
        newQueue=collections.deque()
        newQueue.append(dictionary[node.label])
        visited=set([node])                                                         #record whether node is visited
        while currentQueue:
            currentNode=currentQueue.popleft()
            newNode=newQueue.popleft()
            for n in currentNode.neighbors:                                         #process every node's neighbors
                if n.label not in dictionary:
                    dictionary[n.label]=UndirectedGraphNode(n.label)                #add to dictionary
                newNode.neighbors.append(dictionary[n.label])                       #add neighbors to new current node
                if n not in visited:                                                #add unvisited nodes to deque
                    currentQueue.append(n)
                    newQueue.append(dictionary[n.label])
                    visited.add(n)
        return dictionary[node.label]
