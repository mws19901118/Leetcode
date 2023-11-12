class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:                                                  #If source and target is same, no need to take any bus.
            return 0
        stops, adjacentList = defaultdict(set), defaultdict(list)             #Initialize the routes of each stop, and the adjacent list of routes.
        for i, r in enumerate(routes):                                        #Traverse routes.
            for x in r:                                                       #Traverse stops in current route.
                for j in stops[x]:                                            #For all routes already exist for current stop, build an edge between it and current route.
                    adjacentList[i].append(j)
                    adjacentList[j].append(i)
                stops[x].add(i)                                               #Add i to stops[x].
        if source not in stops or target not in stops:                        #If either source and target not in stops, return -1.
            return -1
        count = 1                                                             #Initialize count.
        q = stops[source]                                                     #Get the initial routes at source.
        visited = set(q)                                                      #Initialize a set for visited routes.
        while q:                                                              #BFS.
            newq = []                                                         #Initialize new queue.
            for x in q:                                                       #Traverse queue.
                if x in stops[target]:                                        #If current route can reach target, return count.
                    return count
                for y in adjacentList[x]:                                     #Traverse the adjacent list of current route.
                    if y not in visited:                                      #If y is not vistied, add y to visited and append y to newq.
                        visited.add(y)
                        newq.append(y)
            q = newq                                                          #Replace q with newq.
            count += 1                                                        #Increase count.
        return -1                                                             #Return -1 if cannot reach target.
