class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adjacentList = defaultdict(set)                                                      #Build adjacent list.
        for a, b in edges:
            adjacentList[a].add(b)
            adjacentList[b].add(a)
        q = set([i for i in range(len(edges) + 1) if len(adjacentList[i]) == 1])             #Find all leaf nodes.
        diameter = 0                                                                         #Initialize diameter.
        while q:                                                                             #BFS topological sort.
            newq = set()                                                                     #Initialize new queue.
            flag = False                                                                     #Indicate if the nodes in q are adjacent with each other; in this case, we can only add 1 to diameter.
            for x in q:                                                                      #Traverse q.
                for y in adjacentList[x]:                                                    #Traverse the neighbors of x.
                    adjacentList[y].remove(x)                                                #Remove x from the adjacent list of y.
                    if len(adjacentList[y]) == 1:                                            #If the adjacent list of y only has 1 node, y becomes a new leaf node so add it to newq.
                        newq.add(y)
                    elif len(adjacentList[y]) == 0:                                          #If the adjacent list of y is empty, we have 2 scenarios.
                        if y in newq:                                                        #If y in newq, it's no longer a leaf node so remove it from newq.
                            newq.remove(y)
                        else:                                                                #Otherwise, it's adjacent with another node in q, so set flag to true.
                            flag = True
            q = newq                                                                         #Replace q with newq.
            diameter += 2 if not flag else 1                                                 #Increase 1 to diameter if nodes in q are adjacent with each other; otherwise increase 2.
        return diameter
