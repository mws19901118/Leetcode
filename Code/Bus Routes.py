class Solution:
    def buildGraph(self, routes):                                                         #Build graph.
        stopSetByRoutes = [set(r) for r in routes]                                        #Convert routes from list of list to list of set.
        graph = [set() for i in range(len(routes))]                                       #Initialize graph to be a list of set.
        for i in range(len(routes)):                                                      #For each pair of routes, if their stop set has intersection, meaning the 2 routes are connected, so, add the index of route to each other's graph set.
            for j in range(i + 1, len(routes)):
                if stopSetByRoutes[i] & stopSetByRoutes[j]:
                    graph[i].add(j)
                    graph[j].add(i)
        return stopSetByRoutes, graph
    
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:                                                                        #If S and T is same, return 0.
            return 0
        stopSetByRoutes, graph = self.buildGraph(routes)                                  #Build graph.
        q = set([i for i, stopSet in enumerate(stopSetByRoutes) if S in stopSet])         #Initialize q to be the set of routes which has S.
        visited = set()                                                                   #Initialize visied to be an empty set.
        count = 1                                                                         #Initialize count to be 1.
        while q:                                                                          #While we have routes to take, do iteration.
            visited |= q                                                                  #Add all routes in this iteration to visited.
            nextq = set()                                                                 #Initialize routes to take for next iteration.
            for route in q:                                                               #For each route, if T in its stop set, return count.
                if T in stopSetByRoutes[route]:
                    return count
                for r in graph[route]:                                                    #Add all connected routes to nextq if not in visited.
                    if r not in visited:
                        nextq.add(r)
            q = nextq                                                                     #Update q to be nextq.
            count += 1                                                                    #Increase count by 1.
        return -1                                                                         #Return -1 if we cannot reach T.
