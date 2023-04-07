class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])                                                          #Similar with Number of Closed Islands.
        count = 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] != 1:
                continue
            q = [(i, j)]
            grid[i][j] = -1
            size = 0
            reachEdge = False
            while q:
                newq = []
                for x, y in q:
                    size += 1                                                                   #Just need to track the size of each island.
                    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            newq.append((nx, ny))
                            grid[nx][ny] = -1
                        elif nx == -1 or nx == m or ny == -1 or ny == n:
                            reachEdge = True
                q = newq
            count += int(not reachEdge) * size                                                  #Add size to count only when current island cannot reach the edge.
        return count
