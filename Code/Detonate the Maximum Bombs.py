class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacentList = defaultdict(list)                                                        #Initialize adjacent list.
        for i, (x, y, r) in enumerate(bombs):                                                   #Traverse bombs, and build adjacent list for each bomb.
            for j, (xx, yy, rr) in enumerate(bombs):
                if i == j:
                    continue
                if (x - xx) ** 2 + (y - yy) ** 2 <= r ** 2:                                     #If bomb[j] is in the blast radius of bomb[i], add j to adjacentList[i].
                    adjacentList[i].append(j)
                    
        def DFS(curr: int, visited: set) -> int:                                                #DFS.
            visited.add(curr)                                                                   #Add curr to visited.
            return 1 + sum(DFS(x, visited) for x in adjacentList[curr] if x not in visited)     #Return the sum of all DFS result from each unvisited neighbor plus 1.

        return max(DFS(i, set()) for i in range(len(bombs)))                                    #Return the max of DFS result from each bomb.
