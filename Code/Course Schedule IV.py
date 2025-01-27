class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacentList = defaultdict(list)                                                    #Build graph.
        for x, y in prerequisites:
            adjacentList[x].append(y)
        isPrerequisite = [[False for _ in range(numCourses)] for  _ in range(numCourses)]   #Initialize the isPrerequisite matrix between each 2 nodes.
        visited = set()                                                                     #Store vivisted nodes.
        def DFS(x: int) -> None:                                                            #DFS to populate isPrerequisite matrix from node x.
            for y in adjacentList[x]:                                                       #Traverse the neighbors of x.
                isPrerequisite[x][y] = True                                                 #X is prerequisite for y.
                if y not in visited:                                                        #If y is not visited, keep DFS from y.
                    DFS(y)
                for i in range(numCourses):                                                 #Merge isPrerequisite[y] with isPrerequisite[x] in an OR fashion.
                    isPrerequisite[x][i] |= isPrerequisite[y][i]
            visited.add(x)

        for i in range(numCourses):                                                         #Traverse numCourses.
            if i in visited:                                                                #Skip visited nodes.
                continue
            DFS(i)                                                                          #DFS from i.
        return [isPrerequisite[x][y] for x, y in queries]                                   #Return the result of each query.
