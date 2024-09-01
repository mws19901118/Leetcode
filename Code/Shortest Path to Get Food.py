class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])                                                                #Get dimensions.
        q = [(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == '*']                     #Find starting point.
        count = 1
        while q:                                                                                      #BFS.
            newq = []
            for x, y in q:
                for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                    if 0 <= u < m and 0 <= v < n and grid[u][v] != 'X' and grid[u][v] != '*':
                        if grid[u][v] == '#':                                                         #If reaches food, return count.
                            return count
                        grid[u][v] = '*'
                        newq.append((u, v))
            q = newq
            count += 1
        return -1                                                                                     #Return -1 at the end.
