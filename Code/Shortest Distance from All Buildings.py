class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        distance = [[0 for j in xrange(n)] for i in xrange(m)]                #Store the sum of distances to all buildings.
        reachable = [[False for j in xrange(n)] for i in xrange(m)]           #Indicate if current land can be access from all buildings.
        buildings = []                                                        #Store the coordinates of all buildings.
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                elif grid[i][j] == 0:                                         #Only empty lands are reachable.
                    reachable[i][j] = True
        for c in buildings:                                                   #BFS starting from every building.
            visited = [[False for j in xrange(n)] for i in xrange(m)]         #Record if current land is visited in current BFS.
            visited[c[0]][c[1]] = True
            q = [c]
            step = 0
            while q != []:
                l = len(q)                                                    #Get the length of nodes in current level.
                for i in range(l):                                            #Check every land in current level.
                    t = q[i]
                    distance[t[0]][t[1]] += step                              #Add to sum of distances.
                    for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:              #Go to the 4 directions.
                        x = t[0] + d[0]
                        y = t[1] + d[1]
                        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 0 and visited[x][y] is False:
                            q.append((x, y))                                  #If current land is valid and unvisited, append current land to q.
                            visited[x][y] = True                              #Set curent land as visited.
                step += 1                                                     #Increase step by 1.
                q = q[l:]                                                     #Update q to next level.
            for i in xrange(m):
                for j in xrange(n):
                    if visited[i][j] is False:                                #If we can't reach a land in current BFS, it's not possible to build house there.
                        reachable[i][j] = False
        shortest = 0x7fffffff
        for i in xrange(m):
            for j in xrange(n):
                if reachable[i][j] is True:
                    shortest = min(shortest, abs(distance[i][j]))             #Find the shortest distance.
        if shortest == 0x7fffffff:
            return -1                                                         #If can't find, return -1.
        return shortest
