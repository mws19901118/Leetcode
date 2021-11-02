class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        labels = [None] * len(graph)                            #Assign a label to each node, initially none.
        unvisited = set([_ for _ in range(len(graph))])         #Put all nodes in a set, meaning the nodes that are unvisited.
        while unvisited:                                        #Do BFS while there are unvisited nodes.
            q = random.sample(unvisited, 1)                     #Randomly choose one node from unvisited and put it in a queue.
            labels[q[0]] = 0                                    #Label it 0.
            while q:                                            #BFS.
                newq = []                                       #Initialize new queue.
                for x in q:                                     #Traverse q.
                    unvisited.remove(x)                         #Remove x from unvisited.
                    for y in graph[x]:                          #Traverse the neighbors of x.
                        if labels[y] == labels[x]:              #If x and y have same label, the partition is invalid, so return false.
                            return False
                        if labels[y] is None:                   #If y's label is none, assign the opposite label of x to it and append it to newq.
                            labels[y] = 1 - labels[x]
                            newq.append(y)
                q = newq                                        #Replace q with newq.
        return True                                             #Return true at the end, which means all nodes have been visited and there graph is bipartite.
