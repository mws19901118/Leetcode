class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = [None] * len(graph)                                                  #Store if each node is safe or not.
        def DFS(x: int, visited: Set[int]) -> bool:                                   #DFS to determine if given node is safe.
            if isSafe[x] is not None:                                                 #If we already know if x is safe, directly return isSafe[x].
                return isSafe[x]
            if x in visited:                                                          #If x is visited, there is a cycle, set isSafe[x] to false and return it.
                isSafe[x] = False
                return False
            visited.add(x)                                                            #Add x to visited.
            isSafe[x] = not graph[x] or all(DFS(y, visited) for y in graph[x])        #If x has no outgoing edge or all nodes that outgoing edges are pointing to are safe o\nodes, x is safe.
            visited.remove(x)                                                         #Remove x from visited.
            return isSafe[x]                                                          #Return isSafe[x].

        for i in range(len(graph)):                                                   #Traverse graph and start DFS from each node.
            DFS(i, set())
        return [i for i, x in enumerate(isSafe) if x]                                 #Return the nodes that are safe.
