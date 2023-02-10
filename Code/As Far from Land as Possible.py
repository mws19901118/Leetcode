class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                                                                                                                                              #Get the dimensions.
        q = [(i, j) for i, j in product(range(m), range(n)) if not grid[i][j] and any(grid[x][y] == 1 for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)] if 0 <= x < m and 0 <= y < n)]                   #Find all water cells that are adjacent to islands.
        if not q:                                                                                                                                                                                                   #If no such cell, return -1.
            return -1
        visited = set(q)                                                                                                                                                                                            #Initialize all visited cells.
        distance = 0                                                                                                                                                                                                #Initialize distance.
        while q:                                                                                                                                                                                                    #BFS.
            newq = []
            for i, j in q:
                for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                        visited.add((x, y))
                        newq.append((x, y))
            q = newq
            distance += 1
        return distance                                                                                                                                                                                             #Return result.
