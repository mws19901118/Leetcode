class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def BFS(x: int, y: int) -> None:                                                                    #BFS.
            q = [(x, y)]                                                                                    #Put starting land in a queue.
            distance = 0                                                                                    #Initialize distance.
            while q:                                                                                        #BFS until queue is not empty.
                newq = []                                                                                   #Initialize new queue.
                for x, y in q:                                                                              #Travrese coordinates in queue.
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                           #Traverse each neightbor.
                        if 0 <= u < m and 0 <= v < n and grid[u][v] == -(buildingCount - 1):                #If neighbor is valid and can reach (buildingCount - 1) buildings, it could be a valid land to build house.
                            grid[u][v] -= 1                                                                 #Mark it as can reach buildingCount buildings.
                            newq.append((u, v))                                                             #Append it to new queue.
                            distanceSum[(u, v)] += distance + 1                                             #Add the distance from it to the starting building to its distance sum.
                q = newq
                distance += 1

        m, n = len(grid), len(grid[0])                                                                      #Get the dimensions.
        buildingCount = 0                                                                                   #Count buildings.
        distanceSum = defaultdict(int)                                                                      #Store the distance sum for each valid land in a defaultdict.
        for i, j in product(range(m), range(n)):                                                            #Traverse grid.
            if grid[i][j] == 1:                                                                             #If current coordinate is building, increase building count and start BFS.
                buildingCount += 1
                BFS(i, j)

        validLand = [(x, y) for x, y in distanceSum if grid[x][y] == -buildingCount]                        #Find all valid land to build house.
        return -1 if not validLand else min(distanceSum[(x, y)] for x, y in validLand)                      #Return -1 if no valid land; otherwise return the minimum distance sum of each valid land.
